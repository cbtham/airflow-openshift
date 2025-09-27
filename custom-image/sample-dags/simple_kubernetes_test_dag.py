"""
Simple test DAG for CNCF Kubernetes provider
Tests basic KubernetesPodOperator functionality in the airflow namespace
"""
from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Create the DAG
with DAG(
    dag_id='simple_kubernetes_test',
    default_args=default_args,
    description='Simple test DAG for CNCF Kubernetes provider',
    schedule=None,  # Manual trigger only
    catchup=False,
    tags=['kubernetes', 'test', 'cncf'],
) as dag:

    # Test 1: Simple hello world pod
    hello_world_task = KubernetesPodOperator(
        task_id='hello_world_pod',
        name='hello-world-pod',
        namespace='airflow',  # Use airflow namespace as requested
        image='python:3.11-slim',
        cmds=['python', '-c'],
        arguments=['print("Hello from KubernetesPodOperator in airflow namespace!")'],
        get_logs=True,
        do_xcom_push=False,
        is_delete_operator_pod=True,  # Clean up pod after completion
    )

    # Test 2: Pod with environment variables
    env_test_task = KubernetesPodOperator(
        task_id='env_test_pod',
        name='env-test-pod',
        namespace='airflow',
        image='python:3.11-slim',
        cmds=['python', '-c'],
        arguments=[
            'import os; '
            'print(f"TEST_VAR: {os.getenv(\'TEST_VAR\', \'Not set\')}"); '
            'print(f"AIRFLOW_NAMESPACE: {os.getenv(\'AIRFLOW_NAMESPACE\', \'Not set\')}")'
        ],
        env_vars={
            'TEST_VAR': 'Hello from environment!',
            'AIRFLOW_NAMESPACE': 'airflow'
        },
        get_logs=True,
        do_xcom_push=False,
        is_delete_operator_pod=True,
    )

    # Test 3: Pod with resource limits
    resource_test_task = KubernetesPodOperator(
        task_id='resource_test_pod',
        name='resource-test-pod',
        namespace='airflow',
        image='python:3.11-slim',
        cmds=['python', '-c'],
        arguments=[
            'import psutil; '
            'print(f"CPU count: {psutil.cpu_count()}"); '
            'print(f"Memory: {psutil.virtual_memory().total / (1024**3):.2f} GB")'
        ],
        resources={
            'request_memory': '128Mi',
            'request_cpu': '100m',
            'limit_memory': '256Mi',
            'limit_cpu': '200m'
        },
        get_logs=True,
        do_xcom_push=False,
        is_delete_operator_pod=True,
    )

    # Set task dependencies
    hello_world_task >> env_test_task >> resource_test_task
