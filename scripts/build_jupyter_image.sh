#!/bin/bash

set -e

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WS_ROOT="$( dirname ${CURR_DIR} )"
DOCKERFILE="workspace/jupyter/Dockerfile"
REPO="repo"
NAME="junior-de-lab"
TAG="dev"

# Run docker buildx create --use before running this script
echo "Running: docker buildx build --platform=linux/amd64,linux/arm64 -t $REPO/$NAME:$TAG -f $DOCKERFILE $WS_ROOT --push"
docker buildx build --platform=linux/amd64,linux/arm64 -t $REPO/$NAME:$TAG -f $DOCKERFILE $WS_ROOT --push
