#!/bin/bash

IMAGE_TAR="student-app.tar"

echo "Rozpoczynam audyt bezpieczeństwa obrazu: $IMAGE_TAR"

podman run --rm -v .:/app docker.io/aquasec/trivy:latest image \
  --severity CRITICAL \
  --exit-code 1 \
  --input /app/$IMAGE_TAR
  
EXIT_CODE=$?

if [ $EXIT_CODE -eq 1 ]; then
    echo "[BŁĄD] Wykryto podatności CRITICAL! Zablokowano wdrożenie."
    exit 1
else
    echo "[SUKCES] Obraz jest czysty pod kątem podatności CRITICAL."
    exit 0
fi
