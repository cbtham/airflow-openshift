# Airflow with CNCF Kubernetes Provider Guide

This guide explains how to deploy Apache Airflow with the CNCF Kubernetes provider using a custom Docker image approach. Your custom package should be in a dockerfile.

### 1. Build and Push Custom Docker Image

```bash
# Build the custom image
docker build -t your-registry/airflow-custom:latest .

# Push to your container registry
docker push your-registry/airflow-custom:latest
```

### 2. Update Configuration

Edit `airflow_redhat_values.yaml` and replace:
- `your-registry/airflow-custom` with your actual image repository
- Update the Fernet key with your actual key
- Adjust resource limits as needed

### 3. Deploy to OpenShift/Kubernetes

```bash
# Create the airflow namespace if it doesn't exist
kubectl create namespace airflow

# Deploy using Helm
helm upgrade --install airflow airflow-stable/airflow \
  -f airflow_redhat_values.yaml \
  -n airflow
```

### 4. Test the Deployment

1. Copy the test DAG to your DAGs folder:
   ```bash
   kubectl cp sample-dags/simple_kubernetes_test_dag.py airflow/airflow-scheduler-xxx:/opt/airflow/dags/
   ```

2. Access the Airflow UI and trigger the `simple_kubernetes_test` DAG

3. Verify that pods are created in the `airflow` namespace and complete successfully
</br>

This deployment uses
- Uses `CeleryExecutor` for scalability
- EFS persistence for DAGs and logs
- Proper RBAC configuration for Kubernetes pod operations
- OpenShift-compatible security contexts
- Resource limits and environment variable testing
- You can customize the image with additional packages as needed
