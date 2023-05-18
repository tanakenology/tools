from collections.abc import Generator, Iterable
from dataclasses import dataclass


@dataclass
class CsvPath:
    value: str


@dataclass
class JsonlinesPath:
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
class ReadJsonlinesCondition:
    input_path: JsonlinesPath


@dataclass
class WriteCsvCondition:
    output_path: CsvPath
    iterable: Iterable
    delimiter: Delimiter


@dataclass
class WriteJsonlinesCondition:
    output_path: JsonlinesPath
    iterable: Iterable


@dataclass
class RowGenerator:
    value: Generator[dict[str, str] | list[str], None, None]
