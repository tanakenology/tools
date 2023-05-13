# write_csv_gcs

* GCS のコンテナを "resources/write_csv/gcs/data" をマウントして起動する

## GCS に CSV ファイルを保存する

* "gs://e2e-bucket/e2e_folder/actual.csv" に "list" を保存する
* GCS の "e2e-bucket" バケットの "e2e_folder/actual.csv" ファイルパスに保存されたファイルが "resources/write_csv/gcs/expected.csv" と一致する

___
* GCS のコンテナを停止する
