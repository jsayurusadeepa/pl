# syntax = docker/dockerfile:20.10-dind-rootless

RUN useradd -m -s /bin/sh pl | sh
RUN docker context use rootless | sh

WORKDIR /app

COPY requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

COPY ./app ./app

RUN <<EOF
apt-get update
apt-get install -y --no-install-recommends git
EOF

# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /