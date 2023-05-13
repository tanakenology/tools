# read_jsonlines_s3

* S3 のコンテナを起動する
* S3 に "e2e-bucket" バケットを作成する
* S3 の "e2e-bucket" バケットの "e2e_folder/setup.jsonl" ファイルパスに "resources/read_jsonlines/s3/setup.jsonl" が保存される

## S3 にある jsonlines ファイルを取得する

* jsonlines ファイル "s3://e2e-bucket/e2e_folder/setup.jsonl" を読み込む
* 返り値が "json" と一致する

___
* S3 のコンテナを停止する
