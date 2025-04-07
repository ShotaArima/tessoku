FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    unzip

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-install.sh

# Run the installer then remove it
RUN sh /uv-install.sh && \
    rm /uv-install.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin:${PATH}"