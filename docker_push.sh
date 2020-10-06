#!/bin/bash
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker tag smartvit-feedback_feedback-service lucianosz7/smartvit-feedback
docker push lucianosz7/smartvit-feedback