import csv
import os
from collections.abc import Generator, Iterable

import boto3  # type: ignore
import smart_open  # type: ignore


class CsvDriver:
    @classmethod
    def read(
        cls, input_path: str, delimiter: str, row_as_list: bool
    ) -> Generator:
        with smart_open.open(
            input_path, "r", transport_params=cls.gen_tparams(input_path)
        ) as fin:
            if row_as_list:
                yield from csv.reader(fin, delimiter=delimiter)
            else:
                yield from csv.DictReader(fin, delimiter=delimiter)

    @classmethod
    def write(cls, output_path: str, iterable: Iterable, delimiter: str):
        with smart_open.open(
            output_path, "w", transport_params=cls.gen_tparams(output_path)
        ) as fout:
            writer = csv.writer(fout, lineterminator="\n", delimiter=delimiter)
            writer.writerows(iterable)

    @classmethod
    def gen_tparams(cls, path: str):
        if str(path).startswith("s3://"):
            return {
                "client": boto3.client(
                    "s3",
                    endpoint_url=os.getenv(
                        "AWS_S3_ENDPOINT",
                        default="https://s3.ap-northeast-1.amazonaws.com/",
                    ),
                )
            }
        return {}
