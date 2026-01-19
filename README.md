# 🏦 SecureBank DevSecOps Platform (Local, End-to-End)

## 📌 Overview

**SecureBank DevSecOps** is a fully local, enterprise-grade DevSecOps reference implementation for a **banking-domain microservices platform**.
It demonstrates **secure CI/CD**, **GitOps**, **Kubernetes deployment**, **observability**, and **runtime security**, using only **Docker Desktop Kubernetes** (no cloud dependency).

This repository is designed to **simulate real-world enterprise DevOps practices** while remaining **100% runnable on a developer laptop**.

---

## 🎯 Key Objectives

* End-to-end DevSecOps pipeline (Code → Build → Scan → Deploy)
* Microservices architecture using **FastAPI**
* Kubernetes deployment using **Helm**
* CI/CD using **Jenkins (Docker-based)**
* GitOps deployment using **ArgoCD**
* Security integrated at **every stage**
* Full observability stack (Metrics, Logs, Runtime Security)
* Banking-grade security mindset

---

## 🧱 Architecture (Logical Flow)

```
Developer
  |
  | Git Push / PR
  v
GitHub
  |
  | PR Checks
  | - Lint
  | - Unit Tests
  v
Jenkins (Docker)
  |
  | === DEVSECOPS GATES ===
  | - SonarQube (Code Quality)
  | - Checkmarx (SAST)
  | - Snyk (Dependencies)
  | - Bandit (Python SAST)
  |
  | - Docker Build
  | - Trivy / Snyk (Image Scan)
  |
  v
Docker Desktop Images (Local)
  |
  | GitOps Commit (Helm values update)
  v
ArgoCD
  |
  v
Docker Desktop Kubernetes
  |
  | Runtime Security
  | - Sysdig
  |
  | Observability
  | - Prometheus
  | - Grafana
  | - ELK
```

---

## 📁 Repository Structure

```
securebank-devops/
│
├── apps/                         # FastAPI microservices
│   ├── auth-service/
│   ├── account-service/
│   ├── transaction-service/
│   └── notification-service/
│
├── helm/                         # Helm charts (GitOps source)
│   └── securebank/
│
├── jenkins/                      # Jenkins CI
│   ├── Dockerfile
│   ├── plugins.txt
│   ├── Jenkinsfile
│   └── docker-compose.yml
│
├── security/                     # Security tooling
│   ├── sonarqube/
│   ├── snyk/
│   ├── checkmarx/
│   ├── trivy/
│   └── sysdig/
│
├── observability/                # Monitoring & logging
│   ├── prometheus/
│   ├── grafana/
│   └── elk/
│
├── gitops/
│   └── argocd/
│
├── infrastructure/               # IaC (local-ready)
│   ├── terraform/
│   └── ansible/
│
├── scripts/                      # Helper scripts
│
└── README.md
```

---

## 🧩 Microservices Overview

| Service              | Responsibility            | Port |
| -------------------- | ------------------------- | ---- |
| auth-service         | Authentication & JWT      | 8000 |
| account-service      | Account & balance APIs    | 8001 |
| transaction-service  | Transactions              | 8002 |
| notification-service | Email/SMS alerts (mocked) | 8003 |

---

## 🛠️ Prerequisites (MANDATORY)

Install **before starting**:

* Docker Desktop (enable Kubernetes)
* Git
* curl
* Helm v3+
* kubectl
* GitHub account (PAT configured)

Verify:

```bash
docker version
kubectl version --client
helm version
```

---

## 🐳 STEP 1 — Enable Docker Desktop Kubernetes

Docker Desktop → **Settings → Kubernetes → Enable**

Verify:

```bash
kubectl get nodes
```

---

## 🔐 STEP 2 — Jenkins (Docker-Based)

### 2.1 Build Jenkins Image (with Docker inside)

```bash
cd jenkins
docker compose build
docker compose up -d
```

Access Jenkins:

```
http://localhost:8080
```

---

### 2.2 Jenkins Plugins (Preinstalled)

| Plugin              | Purpose        |
| ------------------- | -------------- |
| Git                 | SCM            |
| Pipeline            | CI pipelines   |
| Docker Pipeline     | Docker build   |
| SonarQube Scanner   | Code quality   |
| Blue Ocean          | Pipeline UI    |
| Credentials Binding | Secure secrets |

---

### 2.3 Jenkins Credentials (REQUIRED)

Add these under **Manage Jenkins → Credentials → Global**:

| ID           | Type            |
| ------------ | --------------- |
| github-creds | GitHub PAT      |
| snyk-token   | Snyk API Token  |
| sonar-token  | SonarQube Token |

---

## 🔎 STEP 3 — DevSecOps Tools (Local)

| Tool      | Purpose          |
| --------- | ---------------- |
| SonarQube | Code quality     |
| Bandit    | Python SAST      |
| Checkmarx | Static analysis  |
| Snyk      | Dependency scan  |
| Trivy     | Image scan       |
| Sysdig    | Runtime security |

Each runs **locally via Docker** under `/security`.

---

## 🧪 STEP 4 — Jenkins DevSecOps Pipeline

Pipeline stages:

1. Checkout code
2. Lint & unit tests
3. SonarQube scan
4. Bandit (Python SAST)
5. Snyk dependency scan
6. Docker build (local images)
7. Trivy image scan
8. Helm values update
9. GitOps commit

📍 **Important:**
Images are **NOT pushed to a registry** — Docker Desktop Kubernetes pulls them locally.

---

## ⛵ STEP 5 — Helm Charts

Helm is used for:

* Kubernetes manifests
* Image tag updates via GitOps
* Environment portability

📌 **Best Practice Note**

> Helm charts are kept in the **same repo for learning simplicity**.
> In real enterprises, Helm charts **should live in a separate GitOps repository**.

---

## 🚀 STEP 6 — ArgoCD (GitOps)

### Install ArgoCD

```bash
kubectl create namespace argocd
kubectl apply -n argocd \
  -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

Expose UI:

```bash
kubectl port-forward svc/argocd-server -n argocd 8081:443
```

Access:

```
https://localhost:8081
```

---

### ArgoCD Responsibilities

* Watches Helm repo
* Detects image tag changes
* Syncs to Kubernetes automatically
* Enforces GitOps discipline

---

## 📊 STEP 7 — Observability Stack

| Component  | Purpose                  |
| ---------- | ------------------------ |
| Prometheus | Metrics                  |
| Grafana    | Dashboards               |
| ELK        | Logs                     |
| Sysdig     | Runtime threat detection |

Installed via Helm under `/observability`.

---

## 🔐 Security Coverage (Shift-Left → Runtime)

| Phase        | Tool      |
| ------------ | --------- |
| Code         | SonarQube |
| Code         | Bandit    |
| Dependencies | Snyk      |
| Images       | Trivy     |
| Runtime      | Sysdig    |

This aligns with **banking & regulated industry standards**.

---

## 🌱 Branching Strategy

| Branch | Purpose     |
| ------ | ----------- |
| main   | Production  |
| stage  | Pre-prod    |
| dev    | Development |

GitOps commits are **environment-specific**.

---

## 🧠 Why This Project Matters

This repository demonstrates:

* Real DevOps problem solving
* Enterprise CI/CD patterns
* Security-first design
* Kubernetes-native thinking
* GitOps maturity
* Banking-domain readiness

It is **interview-ready**, **POC-ready**, and **architect-approved**.

---

## 🧭 Next Enhancements (Optional)

* Jenkins agents on Kubernetes
* OPA / Kyverno policies
* Vault for secrets
* Canary deployments
* Multi-cluster GitOps

---

## ✅ Final Status

✔ CI/CD fully working
✔ DevSecOps gates enforced
✔ Kubernetes deployed via Helm
✔ GitOps via ArgoCD
✔ Observability & runtime security enabled
