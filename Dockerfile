FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        bash \
        ca-certificates \
        curl \
        git \
        less \
        nano \
        nodejs \
        npm \
        openssh-client \
        python3 \
        python3-pip \
        ripgrep \
        vim-tiny \
    && rm -rf /var/lib/apt/lists/*

ARG USERNAME=sandbox
ARG USER_UID=1001
ARG USER_GID=1001

RUN groupadd --gid "${USER_GID}" "${USERNAME}" \
    && useradd --uid "${USER_UID}" --gid "${USER_GID}" -m "${USERNAME}" -s /bin/bash

WORKDIR /workspace
RUN chown "${USERNAME}:${USERNAME}" /workspace

USER "${USERNAME}"

CMD ["/bin/bash"]
