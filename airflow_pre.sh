#!/bin/sh
oc adm policy add-scc-to-user anyuid -z airflow-api-server
oc adm policy add-scc-to-user anyuid -z airflow-create-user-job
oc adm policy add-scc-to-user anyuid -z airflow-dag-processor
oc adm policy add-scc-to-user anyuid -z airflow-migrate-database-job
oc adm policy add-scc-to-user anyuid -z airflow-redis
oc adm policy add-scc-to-user anyuid -z airflow-scheduler
oc adm policy add-scc-to-user anyuid -z airflow-statsd
oc adm policy add-scc-to-user anyuid -z airflow-triggerer
oc adm policy add-scc-to-user anyuid -z airflow-worker
oc adm policy add-scc-to-user anyuid -z airflow-webserver
oc adm policy add-scc-to-user anyuid -z default