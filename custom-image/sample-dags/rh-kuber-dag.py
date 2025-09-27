from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from datetime import datetime

with DAG(
    dag_id="redhat_kubernetes_pod_operator_example",
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
    tags=["kubernetes"],
) as dag:
    # Basic example: running a simple 'echo' command in a pod
    run_hello_world = KubernetesPodOperator(
        task_id="redhat_hello_world_pod",
        name="redhat-hello-world-pod",  # Name of the Kubernetes Pod
        namespace="default",  # Kubernetes namespace to create the pod in
        image="ubuntu:latest",  # Docker image to use for the pod
        cmds=["bash", "-cx"],  # Command to execute
        arguments=['echo "Red Hat Hello from KubernetesPodOperator!"'],
        do_xcom_push=False,  # Whether to push xcoms from the pod's stdout
    )

    run_hello_world
