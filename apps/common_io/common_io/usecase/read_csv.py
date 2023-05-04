from common_io.domain import ReadCsvCondition, RowGenerator
from common_io.port.csv_port import CsvPort


class ReadCsvUsecase:
    def __init__(
        self, csv_repository: CsvPort, read_csv_condition: ReadCsvCondition
    ):
        self.csv_repository = csv_repository
        self.read_csv_condition = read_csv_condition

    def execute(self) -> RowGenerator:
        return self.csv_repository.read(self.read_csv_condition)
