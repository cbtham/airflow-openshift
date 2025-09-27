#!/bin/sh
# Security Context Constraints for airflow-redhat namespace
oc adm policy add-scc-to-user anyuid -z airflow-api-server -n airflow-redhat
oc adm policy add-scc-to-user anyuid -z airflow-create-user-job -n airflow-redhat
oc adm policy add-scc-to-user anyuid -z airflow-dag-processor -n airflow-redhat
oc adm policy add-scc-to-user anyuid -z airflow-migrate-database-job -n airflow-redhat
oc adm policy add-scc-to-user anyuid -z airflow-redis -n airflow-redhat
oc adm policy add-scc-to-user anyuid -z airflow-scheduler -n airflow-redhat
oc adm policy add-scc-to-user anyuid -z airflow-statsd -n airflow-redhat
oc adm policy add-scc-to-user anyuid -z airflow-triggerer -n airflow-redhat
oc adm policy add-scc-to-user anyuid -z airflow-worker -n airflow-redhat
oc adm policy add-scc-to-user anyuid -z airflow-webserver -n airflow-redhat
oc adm policy add-scc-to-user anyuid -z default -n airflow-redhat
oc adm policy add-scc-to-user anyuid -z airflow-sa -n airflow-redhat
