# write_jsonlines_gcs

* GCS のコンテナを "resources/write_jsonlines/gcs/data" をマウントして起動する

## GCS に jsonlines ファイルを保存する

* jsonlines ファイルパス "gs://e2e-bucket/e2e_folder/actual.jsonl" に "json" を保存する
* GCS の "e2e-bucket" バケットの "e2e_folder/actual.jsonl" ファイルパスに保存されたファイルが "resources/write_jsonlines/gcs/expected.jsonl" と一致する

___
* GCS のコンテナを停止する
