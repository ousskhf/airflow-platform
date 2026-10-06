"""Example project DAG: runs in the project's own image via DockerOperator.

DAG ids are prefixed with the project name so projects never collide.
"""
from datetime import datetime

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator

with DAG(
    dag_id="hello_project",
    schedule=None,
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["example"],
) as dag:
    DockerOperator(
        task_id="run_in_project_image",
        image="alpine:3",  # replace with your project's image
        command="echo hello from my project image",
        auto_remove="success",
    )
