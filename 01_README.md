# Dockerized Python Data Science Application

## Objective

Build and run a Python/Pandas data processing application inside a Docker container.

The objective is to understand how Docker packages Python applications with their dependencies and provides a consistent execution environment.

## Project Structure

```text
01_python_data_app/
├── app.py
├── data.csv
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md
```

## Application

The application:
- Reads a CSV dataset using Pandas.
- Generates descriptive statistics.
- Performs department-wise aggregation.
- Prints the results.

## Dockerfile

The Dockerfile uses Python 3.12 slim as its base image, installs Pandas, copies the application files and executes app.py.

## Build the Image

```bash
docker build -t ds-summary:v1 .
```

## Run the Container

```bash
docker run --name ds-summary ds-summary:v1
```

## Inspect the Container

```bash
docker ps
docker ps -a
docker logs ds-summary
```

## Remove the Container

```bash
docker rm ds-summary
```

## Verify the Image

```bash
docker images
```

## Key Learnings

Docker Image

- Think of this as a blueprint/template containing your application and its dependencies.

Docker Container

- An instance created from that image. It is where your application actually runs.

1. A Dockerfile defines how an application image is built.
2. Docker images package the application environment and dependencies.
3. Containers are created from images.
4. A container can stop after its main application process finishes.
5. Removing a container does not automatically remove its image.

