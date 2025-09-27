# Custom Airflow image with CNCF Kubernetes provider
# Based on the latest official Apache Airflow image
FROM apache/airflow:3.0.2

# Install the CNCF Kubernetes provider package
# Note: No need to switch users as the base image already uses airflow user
# This is OpenShift compatible as it doesn't require root privileges
RUN pip install --no-cache-dir apache-airflow-providers-cncf-kubernetes==10.8.1

# Verify the installation
RUN pip show apache-airflow-providers-cncf-kubernetes

# Set proper permissions for OpenShift (non-root user)
# The base image already handles this, but we ensure compatibility
USER 50000
