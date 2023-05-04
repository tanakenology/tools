from pathlib import Path

import boto3
from getgauge.python import step

s3_client = boto3.client(
    "s3",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="dummy",
    aws_secret_access_key="dummy",
    region_name="us-east-1",
)


def s3_resource_dir():
    current_dir = Path(__file__).resolve().parent
    return current_dir.parent / "resources" / "read_csv" / "s3"


@step("S3 に <bucket> バケットを作成する")
def create_bucket(bucket: str):
    s3_client.create_bucket(Bucket=bucket)


@step("S3 の <bucket> バケットの <key> ファイルパスに CSV ファイル <file_name> が保存される")
def put_object_to_s3(bucket: str, key: str, file_name: str):
    file_path = s3_resource_dir() / file_name

    s3_client.put_object(
        Bucket=bucket,
        Key=key,
        Body=file_path.read_bytes(),
    )
