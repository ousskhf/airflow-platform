FROM apache/airflow:2.10.5-python3.12
# Keep this image small: project dependencies live in each project's own image
# and run through DockerOperator.
RUN pip install --no-cache-dir apache-airflow-providers-docker
