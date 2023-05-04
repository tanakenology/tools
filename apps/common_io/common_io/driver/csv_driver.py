import csv
import os
from collections.abc import Generator

import boto3  # type: ignore
import smart_open  # type: ignore


class CsvDriver:
    @classmethod
    def read(
        cls, input_path: str, delimiter: str, row_as_list: bool
    ) -> Generator:
        if input_path.startswith("s3://"):
            tparams = {
                "client": boto3.client(
                    "s3",
                    endpoint_url=os.getenv(
                        "AWS_S3_ENDPOINT",
                        default="https://s3.ap-northeast-1.amazonaws.com/",
                    ),
                )
            }
        else:
            tparams = {}
        with smart_open.open(input_path, "r", transport_params=tparams) as fin:
            if row_as_list:
                yield from csv.reader(fin, delimiter=delimiter)
            else:
                yield from csv.DictReader(fin, delimiter=delimiter)
