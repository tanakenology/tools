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


@step("S3 に <bucket> バケットを作成する")
def create_bucket(bucket: str):
    s3_client.create_bucket(Bucket=bucket)


@step("S3 の <bucket> バケットの <key> ファイルパスに <path> が保存される")
def put_object_to_s3(bucket: str, key: str, path: str):
    file_path = Path(__file__).resolve().parent.parent / path

    s3_client.put_object(
        Bucket=bucket,
        Key=key,
        Body=file_path.read_bytes(),
    )


@step("S3 の <bucket> バケットの <key> ファイルパスに保存されたファイルが <path> と一致する")
def assert_object_in_s3(bucket: str, key: str, path: str):
    expected_file_path = Path(__file__).parent.parent / path

    response = s3_client.get_object(Bucket=bucket, Key=key)
    actual = response["Body"].read()
    expected = expected_file_path.read_bytes()

    assert actual == expected
