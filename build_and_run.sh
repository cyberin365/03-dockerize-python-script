#!/bin/bash

# do not forget to 'chmod +x' this file before running it.

# Build the Docker image
docker build -t python_container .

# Run the container, mounting iris.csv for persistence
# --rm is a flag to remove the container after it exits
# -v mounts the current directory's iris.csv into the container
docker run \
	--rm \
	-v "$PWD/iris.csv":/workspace/iris.csv \
	-e MAX_ROWS=5 \
	-e RANDOM_SEED=124 \
	python_container