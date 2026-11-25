# Docker Storage and Image Rebuilding

## 1. Bind Mounts

## Bind Mount in Docker

A **Bind Mount** connects a folder or file from your computer (host) to a location inside a Docker container.

This means both your computer and the container can access the same files.

### Why use it?

- **Local development:** Work on your code directly from your computer.
- **No rebuilding:** Changes made to your source code are immediately accessible inside the container.
- **File sharing:** Share configuration files, datasets, etc. with the container.

### Example (PowerShell)

```powershell
$projectPath = (Get-Location).Path

docker run --rm -it --mount "type=bind,source=$projectPath,target=/app" -w /app ds-summary:v1 bash
```

### Understanding the command

- `$projectPath` → Gets the current folder path on your computer.
- `type=bind` → Specifies that we are using a bind mount.
- `source=$projectPath` → Folder on your computer.
- `target=/app` → Location inside the container.
- `-w /app` → Sets `/app` as the working directory.
- `--rm` → Automatically removes the container when it exits.
- `-it` → Opens an interactive terminal.
- `ds-summary:v1` → Docker image name and tag.
- `bash` → Opens a Bash terminal inside the container.

### Important Note

A bind mount **overlays the target directory** inside the container.

For example, if `/app` already contains files in the Docker image, those files become hidden while the bind mount is active.

They are not deleted; they are simply hidden by the mounted host folder.

### Remember

**Bind Mount = Connect your computer's folder to a container.**

Useful when developing applications because you can edit code on your computer and access those changes inside the container without rebuilding the image.

## 2. Docker Volumes

Volumes provide persistent storage managed by Docker.
Docker Volume allows you to store data outside the container's lifecycle.
Example:

```bash
docker volume create ds-data

docker volume ls

docker volume inspect ds-data

docker run --rm -v ds-data:/data alpine sh -c "echo 'persistent data' > /data/test.txt"

docker run --rm -v ds-data:/data alpine cat /data/test.txt
```

Data survives container removal because it is stored outside the container's writable layer.

## 3. Bind Mount vs Volume

Bind Mount: Connect a folder from your computer to the Docker container.
Volume: Give the container storage managed by Docker.

## 4. Rebuilding Images

Changes made to local source code do not automatically update an existing Docker image.

Rebuild:

```bash
docker build -t ds-summary:v2 .
```

Run:

```bash
docker run --rm ds-summary:v2
```

Image tags help distinguish different builds.

## 5. Image Layers and Caching

Docker builds images using layers corresponding to Dockerfile instructions.

Unchanged layers can be reused from cache.

Recommended pattern:

```dockerfile
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY data.csv .
```

Putting 
```dockerfile
 COPY requirements.txt . 
 ````
before the other file copying is an optimized caching technique, we dont want the same libraries to be installed again for new images. 



This allows dependency installation to be cached when only application code changes.

## 6.  Questions

**Q1. What is the difference between bind mounts and Docker volumes?**

above.

**Q2. What happens to a volume when its container is removed?**

The volume normally remains unless explicitly removed or otherwise managed by a cleanup operation.

**Q3. Why do we rebuild Docker images?**

To incorporate changes in application code, dependencies or image configuration.

**Q4. What is Docker build caching?**

Docker reuses previously built layers when their inputs haven't changed, reducing build time.

**Q5. Why copy requirements.txt before app.py?**

Dependency installation is often more expensive than copying application code. This ordering allows Docker to reuse the dependency layer when source code changes.

## 7. My understanding

## 7. My Understanding

- **Bind Mounts:** Useful during development because changes made to local files are accessible inside the container.
- **Docker Volumes:** Used to store data permanently, even when a container is deleted.
- **Image Rebuilding:** Creates an updated image when application code or dependencies change.
- **Build Caching:** Saves time by reusing previously built layers instead of repeating unchanged steps.

**Key takeaway:** Bind Mounts help with development, Volumes help with persistent storage, and Build Caching makes image rebuilding faster.