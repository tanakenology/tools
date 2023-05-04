import subprocess
from pathlib import Path

from getgauge.python import step


@step("S3 のコンテナを起動する")
def start_s3_container():
    subprocess.run(
        [
            "docker",
            "run",
            "--rm",
            "--name",
            "s3-mock",
            "-itd",
            "-p",
            "4566:4566",
            "-p",
            "4510-4559:4510-4559",
            "-e",
            "AWS_ACCESS_KEY_ID=test",
            "-e",
            "AWS_SECRET_ACCESS_KEY=test",
            "-e",
            "AWS_DEFAULT_REGION=ap-northeast-1",
            "localstack/localstack",
        ]
    )


@step("S3 のコンテナを停止する")
def stop_s3_container():
    subprocess.run(["docker", "stop", "s3-mock"])


@step("GCS のコンテナを起動する")
def start_gcs_container():
    data_path = (
        Path(__file__).parent.parent
        / "resources"
        / "read_csv"
        / "gcs"
        / "data"
    )
    print(data_path)
    subprocess.run(
        [
            "docker",
            "run",
            "--rm",
            "--name",
            "gcs-mock",
            "-d",
            "-p",
            "4443:4443",
            "-v",
            f"{str(data_path)}:/data",
            "fsouza/fake-gcs-server",
            "-scheme",
            "http",
        ]
    )


@step("GCS のコンテナを停止する")
def stop_gcs_container():
    subprocess.run(["docker", "stop", "gcs-mock"])
