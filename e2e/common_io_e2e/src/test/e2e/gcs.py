from pathlib import Path

from getgauge.python import step
from google.cloud import storage

client = storage.Client()


@step("GCS の <bucket> バケットの <key> ファイルパスに保存されたファイルが <path> と一致する")
def assert_object_in_gcs(bucket: str, key: str, path: str):
    expected_file_path = Path(__file__).resolve().parent.parent / path

    blob = client.bucket(bucket).blob(key)
    actual = blob.download_as_bytes()
    expected = expected_file_path.read_bytes()

    assert actual == expected
