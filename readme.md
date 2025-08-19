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

### Post deploy
Comment out this 3 line for statefulset, airflow-postgresql
```yaml
   # RunAsUser: 1001
   # scccompProfile:
   #     type: RuntimeDefault
```
>Note: Without this it will not run.

## WIP Preload DAG on startup with S3 Object store

Option 1: Side car mount - s3-sync

```yaml
dags:
  ## the airflow dags folder##
  path: /opt/airflow/dags
  ...
  s3Sync:
  ## if the git-sync sidecar container is enabled
  enable: true
  ## AWS CLI Docker Image
  image:
    repository: amazon/aws-cli
    tag: latest
    pullPolicy: Always
    # Run as root user
    uid: 65533
    gid: 65533
    # s3 bucket that contains DAG files 
    bucketName: airflow
    # s3 key path to DAG files
    key: dags
    # sync interval in second
    interval: 1803ew98aq7yt
```

Option 2: Pre-load in PV