FROM jenkins/jenkins:lts-jdk17

USER root

# Install dependencies
RUN apt-get update && apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    apt-transport-https \
    git \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# --------------------
# Install Docker CLI
# --------------------
RUN curl -fsSL https://get.docker.com | sh

# --------------------
# Install Helm
# --------------------
RUN curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# --------------------
# Jenkins Plugins
# --------------------
# COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
# RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt

# Fix permissions
RUN usermod -aG docker jenkins

USER jenkins
