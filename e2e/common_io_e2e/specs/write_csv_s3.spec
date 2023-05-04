# write_csv_s3

* S3 のコンテナを起動する
* S3 に "e2e-bucket" バケットを作成する

## S3 に CSV ファイルを保存する

* "s3://e2e-bucket/e2e_folder/actual.csv" に "list" を保存する
* S3 の "e2e-bucket" バケットの "e2e_folder/actual.csv" ファイルパスに保存されたファイルが "resources/write_csv/s3/expected.csv" と一致する

___
* S3 のコンテナを停止する
