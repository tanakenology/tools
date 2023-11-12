# read_csv_gcs
Tags: unimplemented

TODO: CsvDriver で requests.exceptions.ChunkedEncodingError

GCS のコンテナを "resources/read_csv/gcs/data" をマウントして起動する

## GCS にある CSV ファイルを Json として取得する

"gs://e2e-bucket/e2e_folder/setup.csv" を json として読み込む
返り値が "json" と一致する

## GCS にある CSV ファイルを List として取得する

"gs://e2e-bucket/e2e_folder/setup.csv" を list として読み込む
返り値が "list" と一致する

___
GCS のコンテナを停止する
