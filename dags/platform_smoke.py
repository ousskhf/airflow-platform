"""Smoke test for the platform: Airflow can start a container through the Docker socket."""
from datetime import datetime

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator

with DAG(
    dag_id="platform_smoke",
    schedule=None,
    start_date=datetime(2026, 10, 1),
    catchup=False,
    tags=["platform"],
) as dag:
    DockerOperator(
        task_id="hello_from_container",
        image="alpine:3",
        command="echo hello from a project container",
        auto_remove="success",
    )
