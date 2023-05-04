# read_csv_s3

* S3 のコンテナを起動する
* S3 に "e2e-bucket" バケットを作成する
* S3 の "e2e-bucket" バケットの "e2e_folder/setup.csv" ファイルパスに "resources/read_csv/s3/setup.csv" が保存される

## S3 にある CSV ファイルを Json として取得する

* "s3://e2e-bucket/e2e_folder/setup.csv" を json として読み込む
* 返り値が "json" と一致する

## S3 にある CSV ファイルを List として取得する

* "s3://e2e-bucket/e2e_folder/setup.csv" を list として読み込む
* 返り値が "list" と一致する

___
* S3 のコンテナを停止する
