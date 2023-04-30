import csv
from collections.abc import Generator

import smart_open  # type: ignore


class CsvDriver:
    @classmethod
    def read(
        cls, input_path: str, delimiter: str, row_as_list: bool
    ) -> Generator:
        with smart_open.open(input_path, "r") as fin:
            if row_as_list:
                yield from csv.reader(fin, delimiter=delimiter)
            else:
                yield from csv.DictReader(fin, delimiter=delimiter)
