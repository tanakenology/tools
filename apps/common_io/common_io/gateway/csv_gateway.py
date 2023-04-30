from common_io.domain import (
    CsvPath,
    Delimiter,
    IsRowAsList,
    ReadCsvCondition,
    RowGenerator,
)
from common_io.driver.csv_driver import CsvDriver
from common_io.port.csv_port import CsvPort


class CsvGateway(CsvPort):
    def read(self, read_csv_condition: ReadCsvCondition) -> RowGenerator:
        return RowGenerator(
            value=CsvDriver.read(
                read_csv_condition.input_path.value,
                delimiter=read_csv_condition.delimiter.value,
                row_as_list=read_csv_condition.is_row_as_list.value,
            )
        )
