import os
from collections.abc import Generator, Iterable

import boto3  # type: ignore
import jsonlines
import smart_open  # type: ignore


class JsonlinesDriver:
    @classmethod
    def read(cls, input_path: str) -> Generator:
        with smart_open.open(
            input_path, "r", transport_params=cls.gen_tparams(input_path)
        ) as fin:
            for d in jsonlines.Reader(fin):
                yield d

    @classmethod
    def write(cls, output_path: str, iterable: Iterable):
        with smart_open.open(
            output_path, "w", transport_params=cls.gen_tparams(output_path)
        ) as fout:
            jsonlines.Writer(fout).write_all(iterable)

    @classmethod
    def gen_tparams(cls, path: str):
        if path.startswith("s3://"):
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
