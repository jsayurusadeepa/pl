# syntax = docker/dockerfile:1.4
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim AS builder

WORKDIR /app

COPY requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

RUN <<EOF
useradd -s /bin/bash -m pl
groupadd docker
usermod -aG docker pl
EOF

COPY ./app ./app

FROM builder as dev-envs

RUN <<EOF
apt-get update
apt-get install -y --no-install-recommends git
EOF

# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /