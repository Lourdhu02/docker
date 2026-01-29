
````md
# Docker Basics – From Scratch

This document covers the fundamental concepts and hands-on implementation of Docker on Windows, starting from zero and progressing to running real containers.

---

## 1. What is Docker?

Docker is a platform that allows you to package an application along with all its dependencies into a single unit called a **container**.  
This container can run consistently across different environments such as development, testing, and production.

### Problems Docker Solves
- Dependency conflicts
- Environment inconsistency
- “Works on my machine” issues
- Complex setup for applications

---

## 2. Core Docker Concepts

### Image
- A read-only template used to create containers
- Contains application code, libraries, and dependencies
- Examples: `ubuntu`, `nginx`, `python:3.10`

### Container
- A running instance of an image
- Isolated, lightweight, and fast to start
- Can be started, stopped, and deleted

### Docker Engine
- Background service that builds and runs containers
- Communicates with the OS kernel

---

## 3. Installing Docker on Windows

### Prerequisites
- Windows 10 or 11 (64-bit)
- Virtualization enabled in BIOS

---

### Step 1: Install and Enable WSL 2

Open PowerShell as Administrator:

```powershell
wsl --install
````

Restart the system.

Set WSL 2 as default:

```powershell
wsl --set-default-version 2
```

Verify:

```powershell
wsl --status
```

---

### Step 2: Install Docker Desktop

1. Download Docker Desktop from the official website.
2. During installation:

   * Enable WSL 2 backend
   * Use Linux containers
3. Launch Docker Desktop and wait until the Docker Engine is running.

---

## 4. Verifying Docker Installation

Check Docker version:

```powershell
docker --version
```

Run the test container:

```powershell
docker run hello-world
```

Expected result:

* Docker pulls the image
* Creates a container
* Executes it successfully
* Displays a confirmation message

---

## 5. Container Lifecycle

List containers:

```powershell
docker ps        # running containers
docker ps -a     # all containers
```

The `hello-world` container exits automatically after execution.

---

## 6. Running an Interactive Linux Container

Run Ubuntu interactively:

```powershell
docker run -it ubuntu bash
```

Inside the container, you can execute Linux commands:

```bash
ls
pwd
cat /etc/os-release
```

Exit the container:

```bash
exit
```

---

## 7. Running a Background Service (Nginx)

Start an Nginx web server in detached mode:

```powershell
docker run -d -p 8080:80 nginx
```

Explanation:

* `-d` runs the container in background
* `-p 8080:80` maps host port 8080 to container port 80

Access the application in a browser:

```
http://localhost:8080
```

---

## 8. Port Mapping

Port mapping allows services inside a container to be accessible from the host system.

Format:

```
-host_port:container_port
```

Example:

```
8080 (host) → 80 (container)
```

---

## 9. Managing Containers

Stop a container:

```powershell
docker stop <container_id>
```

Remove a container:

```powershell
docker rm <container_id>
```

List images:

```powershell
docker images
```

Remove an image:

```powershell
docker rmi <image_id>
```

---

## 10. Summary

By completing this guide, you have learned:

* What Docker is and why it is used
* Difference between images and containers
* How to install Docker on Windows using WSL 2
* How to run containers interactively and in background
* How port mapping works
* Basic Docker commands for container management


