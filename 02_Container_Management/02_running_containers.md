# Running and Managing Docker Containers

## 1. Running a container in the background

```bash
docker run -d --name my-nginx -p 8080:80 nginx
```

- `-d`: Detached mode; runs in the background.
- `--name`: Assigns a container name.
- `-p`: Maps a host port to a container port.

## 2. Port Mapping

Syntax:

```bash
-p HOST_PORT:CONTAINER_PORT
```

Example:

```bash
docker run -d -p 8080:80 nginx
```

Requests to localhost:8080 are forwarded to port 80 inside the container.

Important: `EXPOSE` in a Dockerfile documents a container port; it does not itself publish that port to the host.

## 3. Inspecting Containers

```bash
docker ps
docker ps -a
docker logs my-nginx
docker inspect my-nginx
```

- `docker ps`: Running containers.
- `docker ps -a`: All containers.
- `docker logs`: Application/container output.
- `docker inspect`: Detailed configuration and runtime information.

## 4. Executing Commands Inside Containers

```bash
docker exec -it my-nginx bash
```

`docker exec` runs a command inside an already-running container.

Some minimal images don't contain Bash. In that case, try:

```bash
docker exec -it my-nginx sh
```

## 5. Container Lifecycle

```bash
docker stop my-nginx
docker start my-nginx
docker restart my-nginx
docker rm my-nginx
```

Stopping a container does not remove it.

Removing a container does not automatically remove its image.

## 6. Automatically Removing Containers

```bash
docker run --rm nginx
```

The container is automatically removed after it exits.

## 7.  Questions

**Q1. What is the difference between `docker run` and `docker start`?**

`docker run` creates a new container from an image and starts it. `docker start` starts an existing stopped container.

**Q2. What is detached mode?**

It runs the container in the background without keeping the terminal attached to its output.

**Q3. What does port mapping do?**

It forwards traffic from a host port to a container port.

**Q4. What is the difference between `docker exec` and `docker run`?**

`docker exec` runs an additional command in an existing running container. `docker run` creates a new container.

**Q5. Why use `--rm`?**

To automatically clean up a container after its process exits.