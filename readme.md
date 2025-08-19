# Deploys latest Airflow on Openshift

## Add Helm Repo
```shell
helm repo add apache-airflow https://airflow.apache.org
```

## Deployment
Run these before deploy,

```shell
oc new project airflow
oc project airflow
oc adm policy add-scc-to-user anyuid -z airflow-api-server
oc adm policy add-scc-to-user anyuid -z airflow-create-user-job
oc adm policy add-scc-to-user anyuid -z airflow-dag-processor
oc adm policy add-scc-to-user anyuid -z airflow-migrate-database-job
oc adm policy add-scc-to-user anyuid -z airflow-redis
oc adm policy add-scc-to-user anyuid -z airflow-scheduler
oc adm policy add-scc-to-user anyuid -z airflow-statsd
oc adm policy add-scc-to-user anyuid -z airflow-triggerer
oc adm policy add-scc-to-user anyuid -z airflow-worker
oc adm policy add-scc-to-user anyuid -z default
```
Then run

```shell
helm install airflow apache-airflow/airflow -f custom_values.yaml --namespace airflow
```