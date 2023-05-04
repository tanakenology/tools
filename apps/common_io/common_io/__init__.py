from collections.abc import Generator, Iterable

from common_io.domain import (
    CsvPath,
    Delimiter,
    IsRowAsList,
    ReadCsvCondition,
    WriteCsvCondition,
)
from common_io.gateway.csv_gateway import CsvGateway
from common_io.usecase.read_csv import ReadCsvUsecase
from common_io.usecase.write_csv import WriteCsvUsecase


def read_csv(
    input_path: str,
    delimiter: str = ",",
    row_as_list: bool = False,
) -> Generator[dict[str, str] | list[str], None, None]:
    read_csv_usecase = ReadCsvUsecase(
        CsvGateway(),
        ReadCsvCondition(
            input_path=CsvPath(value=input_path),
            delimiter=Delimiter(value=delimiter),
            is_row_as_list=IsRowAsList(value=row_as_list),
        ),
    )
    return read_csv_usecase.execute().value


def write_csv(
    output_path: str,
    iterable: Iterable,
    delimiter: str = ",",
) -> None:
    write_csv_usecase = WriteCsvUsecase(
        CsvGateway(),
        WriteCsvCondition(
            output_path=CsvPath(value=output_path),
            iterable=iterable,
            delimiter=Delimiter(value=delimiter),
        ),
    )
    write_csv_usecase.execute()
