from __future__ import annotations

import fnmatch
import glob
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
from typing import Annotated

import typer
from tqdm import tqdm


app = typer.Typer(no_args_is_help=True)

PACKAGE_NAME = "{{ cookiecutter.package_name }}"


def validate_source_root(source_root: str) -> None:
    """Validate that the supplied directory is the repository root.

    Parameters
    ----------
    source_root
        Absolute path to the source repository.

    Raises
    ------
    RuntimeError
        If required project files are missing or a root ``setup.py`` exists.
    """
    pyproject_path = os.path.join(source_root, "pyproject.toml")
    package_path = os.path.join(source_root, "src", PACKAGE_NAME)
    setup_path = os.path.join(source_root, "setup.py")

    if not os.path.isfile(pyproject_path):
        raise RuntimeError(
            f"pyproject.toml not found in source directory: {source_root}"
        )

    if not os.path.isdir(package_path):
        raise RuntimeError(
            f"Package directory not found: {package_path}"
        )

    if os.path.exists(setup_path):
        raise RuntimeError(
            "Root setup.py must not exist. "
            "Release builds use pyproject.toml."
        )


def copy_repository(source_root: str, staging_root: str) -> None:
    """Copy the repository into an isolated release staging directory.

    Parameters
    ----------
    source_root
        Repository to copy.
    staging_root
        Destination for the isolated release build.
    """
    shutil.copytree(
        source_root,
        staging_root,
        ignore=shutil.ignore_patterns(
            ".git",
            ".venv",
            ".pytest_cache",
            ".ruff_cache",
            ".tmp",
            "__pycache__",
            "*.egg-info",
            "build",
            "dist",
            "wheelhouse",
        ),
    )


def build_wheels(staging_root: str) -> str:
    """Build a release wheel.

    Parameters
    ----------
    staging_root
        Isolated release source directory.

    Returns
    -------
    str
        Directory containing the generated wheels.
    """
    wheelhouse = os.path.join(staging_root, "wheelhouse")

    subprocess.run(
        [
            sys.executable,
            "-m",
            "build",
            ".",
            "--wheel",
            "--outdir=wheelhouse",
        ],
        cwd=staging_root,
        check=True,
    )

    return wheelhouse


def verify_release_wheel(wheel_path: str) -> None:
    """Verify that a release wheel does not contain compiled artifacts.

    Parameters
    ----------
    wheel_path
        Wheel to inspect.

    Raises
    ------
    RuntimeError
        If generated C sources or compiled extensions are present.
    """
    with zipfile.ZipFile(wheel_path) as archive:
        names = archive.namelist()

    c_sources = set(fnmatch.filter(names, "*.c"))

    compiled_extensions = set(fnmatch.filter(names, "*.so"))
    compiled_extensions.update(
        fnmatch.filter(names, "*.pyd")
    )

    if c_sources:
        raise RuntimeError(
            "Release wheel contains generated C source files: "
            f"{sorted(c_sources)}"
        )

    if compiled_extensions:
        raise RuntimeError(
            "Release wheel contains compiled extension files: "
            f"{sorted(compiled_extensions)}"
        )


def publish_wheels(
    wheelhouse: str,
    output_directory: str,
) -> None:
    """Verify and copy release wheels to the requested output directory.

    Parameters
    ----------
    wheelhouse
        Temporary build output directory.
    output_directory
        Final directory receiving verified wheels.

    Raises
    ------
    RuntimeError
        If the build produced no wheels.
    """
    wheel_paths = sorted(
        glob.glob(os.path.join(wheelhouse, "*.whl"))
    )

    if not wheel_paths:
        raise RuntimeError("Build produced no wheels.")

    os.makedirs(output_directory, exist_ok=True)

    for wheel_path in tqdm(
        wheel_paths,
        desc="Verifying release wheels",
        unit="wheel",
    ):
        verify_release_wheel(wheel_path)

        destination = os.path.join(
            output_directory,
            os.path.basename(wheel_path),
        )
        shutil.copy2(wheel_path, destination)


@app.command()
def main(
    src: Annotated[
        str,
        typer.Option(
            "--src",
            help="Repository root to build.",
        ),
    ],
    output_dir: Annotated[
        str,
        typer.Option(
            "--output-dir",
            help="Output directory relative to --src.",
        ),
    ] = "wheelhouse",
) -> None:
    """Build release wheels.

    Parameters
    ----------
    src
        Repository root.
    output_dir
        Directory receiving the verified wheels.
    """
    source_root = os.path.abspath(src)

    if os.path.isabs(output_dir):
        final_output = output_dir
    else:
        final_output = os.path.join(source_root, output_dir)

    validate_source_root(source_root)

    with tempfile.TemporaryDirectory(
        prefix="{{ cookiecutter.package_name }}-release-"
    ) as temporary_root:
        staging_root = os.path.join(
            temporary_root,
            "repository",
        )

        copy_repository(
            source_root=source_root,
            staging_root=staging_root,
        )

        wheelhouse = build_wheels(staging_root)

        publish_wheels(
            wheelhouse=wheelhouse,
            output_directory=final_output,
        )

    typer.echo(f"Release wheels written to: {final_output}")


if __name__ == "__main__":
    app()
