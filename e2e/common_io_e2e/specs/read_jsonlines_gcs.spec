# read_jsonlines_gcs
Tags: unimplemented

TODO: CsvDriver で requests.exceptions.ChunkedEncodingError

GCS のコンテナを "resources/read_jsonlines/gcs/data" をマウントして起動する

## GCS にある jsonlines ファイルを取得する

jsonlines ファイル "gs://e2e-bucket/e2e_folder/setup.jsonl" を読み込む
返り値が "json" と一致する

___
GCS のコンテナを停止する
