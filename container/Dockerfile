# Jenkins (track latest LTS) + Docker CLI + Python/pip + Terraform (latest) + Ansible (latest)
FROM jenkins/jenkins:lts-jdk21

USER root
ARG DEBIAN_FRONTEND=noninteractive

# Base OS tools + Python/pip + helpful CLI tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    unzip \
    git \
    jq \
    openssh-client \
    sshpass \
    python3 \
    python3-pip \
 && install -m 0755 -d /etc/apt/keyrings \
 \
 # Docker CLI repo (as you had)
 && curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc \
 && chmod a+r /etc/apt/keyrings/docker.asc \
 && echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian $(. /etc/os-release && echo \"$VERSION_CODENAME\") stable" \
    > /etc/apt/sources.list.d/docker.list \
 \
 # HashiCorp repo for latest Terraform
 && curl -fsSL https://apt.releases.hashicorp.com/gpg | gpg --dearmor -o /etc/apt/keyrings/hashicorp.gpg \
 && chmod a+r /etc/apt/keyrings/hashicorp.gpg \
 && echo "deb [signed-by=/etc/apt/keyrings/hashicorp.gpg] https://apt.releases.hashicorp.com $(. /etc/os-release && echo \"$VERSION_CODENAME\") main" \
    > /etc/apt/sources.list.d/hashicorp.list \
 \
 # Install Docker CLI + Terraform (latest from HashiCorp)
 && apt-get update \
 && apt-get install -y --no-install-recommends docker-ce-cli terraform \
 \
 # Latest pip + Ansible (latest from PyPI)
 && python3 -m pip install --no-cache-dir --upgrade pip \
 && python3 -m pip install --no-cache-dir ansible \
 \
 # Cleanup
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Back to jenkins user for runtime + plugin installation
USER jenkins

# Plugins (unpin trilead so it tracks latest; keep your set)
RUN jenkins-plugin-cli --plugins \
    "trilead-api" \
    "ssh-slaves" \
    "ssh-credentials" \
    "credentials" \
    "docker-workflow" \
    "json-path-api" \
    "blueocean"
