from collections.abc import Generator

from common_io.domain import CsvPath, Delimiter, IsRowAsList, ReadCsvCondition
from common_io.gateway.csv_gateway import CsvGateway
from common_io.usecase.read_csv import ReadCsvUsecase


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
