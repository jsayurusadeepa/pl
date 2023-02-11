# syntax = docker/dockerfile:1.4
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim AS builder

WORKDIR /app

COPY requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

COPY ./app ./app

FROM builder as dev-envs

RUN  apt-get update  | sh
RUN  apt-get install -y --no-install-recommends git | sh


RUN useradd  /bin/bash -m pl | sh
RUN groupadd docker | sh
RUN usermod -aG docker pl | sh

# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /