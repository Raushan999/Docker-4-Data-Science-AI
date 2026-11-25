# Docker Compose: FastAPI + PostgreSQL

## 1. Objective

Run a FastAPI application and PostgreSQL database together using Docker Compose.

Instead of starting and managing containers separately, Compose manages both through one configuration file (`docker-compose.yml` or `compose.yaml`).

## 2. Architecture

```text
         Client
           |
           v
     FastAPI Container
           |
           v
   PostgreSQL Container
           |
           v
      Docker Volume
   (Stores database data)
```

## 3. Services

### API (FastAPI)
- Built using our own Dockerfile.
- Runs on port `8000`.
- Gets database connection details through environment variables.

### Database (PostgreSQL)
- Uses the official PostgreSQL Docker image.
- Runs on port `5432`.
- Uses a named volume to save database records.

## 4. Important Concepts

1. **Docker Compose:** Runs and manages multiple containers using one YAML file.
2. **Services:** Each application component (API, database, etc.) is defined as a service.
3. **Networking:** Compose creates an internal network so containers can communicate.
4. **Service Names:** Containers can communicate using service names instead of IP addresses. For example, the API connects to the database using `db`.
5. **Volumes:** Store database data even if the container is deleted.
6. **Health Checks:** Check whether a service is actually ready to work.
7. **Environment Variables:** Pass configuration such as database username, password and host without hardcoding them in application code.

## 5. Run the Application

```bash
# Check whether the Compose configuration is valid
docker compose config

# Build images and start all services
docker compose up --build -d

# Check running containers
docker compose ps
```

Open FastAPI documentation:

http://localhost:8000/docs

## 6. Useful Commands

```bash
# View logs of all services
docker compose logs -f

# View only API logs
docker compose logs -f api

# Open terminal inside API container
docker compose exec api bash

# Stop and remove containers and network
docker compose down

# Start existing services again
docker compose up -d
```

## 7. Test Database Persistence

1. Add some records through the API.
2. Stop and remove containers:

```bash
docker compose down
```

3. Start the application again:

```bash
docker compose up -d
```

4. Check your previously stored records.

**Expected result:** Records should still exist because PostgreSQL data is stored in a named Docker volume, not just inside the container.

To delete containers AND named volumes:

```bash
docker compose down -v
```

**Warning:** This also deletes the database data stored in those volumes.

## 8.  Questions

**Q1. What is Docker Compose?**

A tool used to define and run multiple containers together using a single YAML configuration file.

**Q2. How do containers communicate in Docker Compose?**

Through an automatically created network. They can use service names as hostnames.

**Q3. Why use volumes with PostgreSQL?**

To preserve database records even when the PostgreSQL container is deleted or recreated.

**Q4. Does `depends_on` guarantee that the database is ready?**

No. Basic `depends_on` controls startup order. A health check with `condition: service_healthy` can make the API wait until the database is healthy.



## 9. My Understanding

Docker Compose allows me to run my complete application (FastAPI + PostgreSQL) using one configuration file.

It manages the containers, connects them through an internal network, and uses volumes to preserve database data.

**Key takeaway:** Compose simplifies running and managing multiple connected containers together.