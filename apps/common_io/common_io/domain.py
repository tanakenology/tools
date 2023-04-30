from collections.abc import Generator
from dataclasses import dataclass
from typing import Sequence


@dataclass
class CsvPath:
    value: str


@dataclass
class Delimiter:
    value: str


@dataclass
class IsRowAsList:
    value: bool


@dataclass
class ReadCsvCondition:
    input_path: CsvPath
    delimiter: Delimiter
    is_row_as_list: IsRowAsList


@dataclass
class RowGenerator:
    value: Generator[dict[str, str] | list[str], None, None]
