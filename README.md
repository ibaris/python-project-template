# Python project template

Cookiecutter template for Python packages using a `src` layout, with project resources organized like Asgard.

## Generate a project

Install Cookiecutter and run it from this repository:

```console
python -m pip install cookiecutter jinja2-time
cookiecutter .
```

For example, choose `Example Library` as the project name to generate an `example-library` repository containing the `example_library` package. Package metadata, CLI entrypoints, Conda environments, documentation, and release tooling use the names selected during generation.

## Generated structure

```text
<repo_name>/
    pyproject.toml
    README.md
    AGENTS.md
    MANIFEST.in
    src/
        <package_name>/
            __init__.py
            __main__.py
            cli.py
        .info/
            AUTHORS.md
            CHANGELOG.md
    tests/
        test_<package_name>.py
    resources/
        configs/
        docs/
            conf.py
            index.rst
            reference/
            requirements.txt
        envs/
            <package_name>.yml
        images/
        scripts/
            deploy.py
    .github/workflows/
    .vscode/settings.json
```

Add application modules under `src/<package_name>` and corresponding tests under `tests`. Keep documentation, environment definitions, example configurations, images, and maintenance scripts under `resources`. Files needed at runtime belong inside the importable package and must be declared as package data in `pyproject.toml`.

## Develop a generated project

Run these commands from the generated repository:

```console
conda env create -f resources/envs/<package_name>.yml
conda activate <package_name>
python -m pip install -e ".[dev,docs]"
python -m pytest
lint-imports
python -m ruff check .
python -m sphinx -b html resources/docs build/docs
```

The import rule prevents the CLI from importing `__main__`, keeping the console script and `python -m <package_name>` entrypoints reusable. Add package-specific import contracts as the library grows.

## Build and release

```console
python resources/scripts/deploy.py --src . --output-dir wheelhouse
```

The release script copies the project into temporary staging, builds a standard Python wheel using `pyproject.toml`, checks for generated C sources and compiled extensions, and copies the verified wheel into `wheelhouse`.

GitHub workflows validate changes, increment calendar versions on `release-candidate`, and build and publish releases from `main`. Before using the deployment workflow, configure its package index destination and credentials. The template currently carries the Wasabi S3 index settings used by the reference project.

The original upstream template documentation is retained in `README.rst`; use this README for the current layout and commands.
