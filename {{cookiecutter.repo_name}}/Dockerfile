FROM continuumio/miniconda3 AS develop
WORKDIR /app
SHELL ["/bin/bash", "--login", "-c"]
RUN apt-get update && apt-get install -y gcc
RUN conda init bash
COPY ./envs/{{cookiecutter.project_env_file}}.yml ./envs/conda-env.yml
RUN conda update -y conda && conda env create -f resources/envs/conda-env.yml --solver=libmamba

FROM develop as build_wheel
COPY . .
RUN conda activate {{cookiecutter.project_env_name}} && pip install --no-build-isolation -e . && python ./scripts/deploy.py --wheel --no-lic