# Contapache

A Python-based automation tool for containerized web server deployment.

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![Docker](https://img.shields.io/badge/docker-required-blue.svg)

## Overview

**Contapache** automates the complete lifecycle of containerized Apache HTTP Server deployment using Python and Docker. This project demonstrates Infrastructure as Code (IaC) principles by programmatically orchestrating container operations that traditionally require manual command-line intervention.

The tool streamlines the process of deploying, customizing, and distributing Docker containers. This approach exemplifies modern deployment automation practices where infrastructure provisioning, configuration management, and deployment are scripted for efficiency.

## Presentation

Check out the presentation in this repository to understand more about the Contapache project.

## Educational Context

This project was developed as part of the CY5001 (Cyberspace Technology and Applications) curriculum at Northeastern University, demonstrating practical application of:

- Container orchestration and lifecycle management
- Python-based infrastructure automation
- Programmatic system administration

The project evolved from a manual Docker deployment lab into an automated solution, showcasing how scripting can enhance operational efficiency in cloud and container environments.

## Architecture & Workflow

### High-Level Process Flow

```
┌─────────────────────┐
│  Execute Script     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Pull httpd Image   │ ← Docker Hub
│  from DockerHub     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Deploy Container   │
│  Port Map: 8080:80  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Modify index.html  │
│  via docker exec    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Commit Changes     │
│  Create New Image   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Push to DockerHub  │ → Docker Hub
│  with Custom Tag    │
└─────────────────────┘
```

## Features

### One-Command Deployment
Deploy an Apache web server with custom content in seconds, eliminating manual configuration steps.

### Automated Image Lifecycle
Handles all the workflow: deploy → configure → commit → distribute.


### Registry Management
Can handle DockerHub authentication, image tagging, and repository pushing.

## Installation

### Prerequisites

**System Requirements:**
- Linux-based operating system (Ubuntu 18.04+ recommended)
- Python 3.x
- Docker Engine installed and running
- Docker Hub account

**Python Dependencies:**
```bash
# Install Docker Python SDK
pip3 install docker
```

### Docker Setup

```bash
# Install Docker (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install docker.io -y

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Add user to docker group (optional, avoids sudo)
sudo usermod -aG docker $USER
newgrp docker

# Verify installation
docker --version
docker run hello-world
```

## Usage

### Basic Execution

```bash
python3 contapache.py
```

**Interactive Prompts:**
```
DockerHub user: your_dockerhub_username
DockerHub pass: ••••••••••••
```

### Expected Output

```
Container HTTPDNewImg has started with httpd image.
Index.html has been changed.
New image your_dockerhub_username/httpd-modified:latest committed and pushed to DockerHub.
```

### Verification

**Check running container:**
```bash
docker ps
```

**Access web server:**
```bash
curl localhost:8080
# Or open browser: http://localhost:8080
```

**View Docker Hub:**
Navigate to your Docker Hub account

## Technical Deep Dive

### Docker SDK Operations

The script utilizes the Docker SDK for Python (`docker-py`) to interact with the Docker daemon.

### Index.html Modification Strategy

The script employs a three-step approach for safe file modification:

1. **Write to temporary location** (`/tmp/index.html`)
2. **Copy to target directory** (`/usr/local/apache2/htdocs/`)
3. **Cleanup temporary file**

## Development Process

### Phase 1: Manual Workflow Analysis
- Documented manual Docker operations
- Identified repetitive tasks suitable for automation
- Mapped command-line operations to Python SDK equivalents

### Phase 2: Script Architecture
- Designed modular function structure for each operation phase
- Implemented error handling for network and authentication failures
- Developed containerized execution strategy for file modifications

### Phase 3: Testing & Refinement
- Resolved container naming conflicts through cleanup procedures
- Optimized file modification approach for reliability
- Added user input validation and feedback mechanisms

### Phase 4: Documentation & Presentation
- Created comprehensive usage documentation
- Developed presentation materials explaining architecture
- Recorded demonstration video showcasing functionality

## Use Cases

### DevOps Automation
- Template for automating container-based service deployments
- Foundation for CI/CD pipeline container builds
- Infrastructure-as-Code implementation for web services

### Educational Demonstrations
- Teaching Docker concepts through practical automation
- Illustrating Python's role in system administration
- Demonstrating container lifecycle management

### Rapid Prototyping
- Quick deployment of web server instances for testing
- Automated environment setup for development teams
- Reproducible infrastructure for demos and presentations

### Enterprise Application
While this project demonstrates basic web server deployment, the principles can be extended to:
- LDAP directory service containerization
- Email server (Postfix/Dovecot) automation
- Application stack deployment (LAMP/MEAN/MERN)
- Microservices orchestration

## Future Enhancements

### Planned Features

#### Enhanced Security
- **Image Vulnerability Scanning**: Integrate Trivy or Clair for automated security scanning
- **Secrets Management**: Implement Docker secrets or HashiCorp Vault integration

#### Monitoring & Logging
- **Container Health Checks**: Implement automated health monitoring endpoints
- **Log Aggregation**: ELK stack or Splunk integration for centralized logging

#### Advanced Functionality
- **Multi-Container Deployments**: Support for application stacks (web + database + cache)

#### Usability Improvements
- **CLI Argument Parsing**: Enhanced command-line interface with argparse
- **Configuration Files**: YAML/JSON-based configuration for deployment parameters

## Troubleshooting

### Common Issues

**Issue: "Permission denied while trying to connect to Docker daemon"**
```bash
# Solution: Add user to docker group or use sudo
sudo usermod -aG docker $USER
newgrp docker
```

**Issue: "Container name 'HTTPDNewImg' already in use"**
```bash
# Solution: Remove existing container
docker rm -f HTTPDNewImg
```

**Issue: "Image push denied: authentication required"**
```bash
# Solution: Verify DockerHub credentials
docker login
```

**Issue: "Port 8080 already in use"**
```bash
# Solution: Stop conflicting service or modify script port mapping
sudo lsof -i :8080
docker stop $(docker ps -q --filter "publish=8080")
```

## Resources

**Docker Fundamentals:**
- [Docker Official Documentation](https://docs.docker.com/)
- [Docker SDK for Python](https://docker-py.readthedocs.io/)
- [Dockerfile Best Practices](https://docs.docker.com/develop/dev-best-practices/)

**Container Security:**
- [Docker Security Best Practices](https://docs.docker.com/engine/security/)
- [CIS Docker Benchmark](https://www.cisecurity.org/benchmark/docker)

**DevOps Automation:**
- [The DevOps Handbook](https://itrevolution.com/the-devops-handbook/)
- [Infrastructure as Code Principles](https://www.terraform.io/intro/index.html)

This project demonstrates practical application of:
- Container lifecycle management and orchestration
- Python SDK integration for infrastructure automation
- System administration programming
