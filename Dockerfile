FROM apache/airflow:2.11.2-python3.12
# Keep this image small: project dependencies live in each project's own image
# and run through DockerOperator.
RUN pip install --no-cache-dir apache-airflow-providers-docker
