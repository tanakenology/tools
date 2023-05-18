# write_jsonlines_s3

* S3 のコンテナを起動する
* S3 に "e2e-bucket" バケットを作成する

## S3 に jsonlines ファイルを保存する

* jsonlines ファイルパス "s3://e2e-bucket/e2e_folder/actual.jsonl" に "json" を保存する
* S3 の "e2e-bucket" バケットの "e2e_folder/actual.jsonl" ファイルパスに保存されたファイルが "resources/write_jsonlines/s3/expected.jsonl" と一致する

___
* S3 のコンテナを停止する
