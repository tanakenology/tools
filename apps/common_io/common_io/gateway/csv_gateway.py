from common_io.domain import ReadCsvCondition, RowGenerator, WriteCsvCondition
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

    def write(self, write_csv_condition: WriteCsvCondition) -> None:
        CsvDriver.write(
            write_csv_condition.output_path.value,
            write_csv_condition.iterable,
            delimiter=write_csv_condition.delimiter.value,
        )
