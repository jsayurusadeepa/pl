# syntax =  docker:20.10-dind-rootless
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim AS builder

RUN useradd -m -s /bin/sh pl | sh
RUN docker context use rootless | sh

WORKDIR /app

COPY requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

COPY ./app ./app

FROM builder as dev-envs

RUN <<EOF
apt-get update
apt-get install -y --no-install-recommends git
EOF

# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /