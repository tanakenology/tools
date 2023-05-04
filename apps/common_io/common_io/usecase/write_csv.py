from common_io.domain import WriteCsvCondition
from common_io.port.csv_port import CsvPort


class WriteCsvUsecase:
    def __init__(
        self, csv_repository: CsvPort, write_csv_condition: WriteCsvCondition
    ):
        self.csv_repository = csv_repository
        self.write_csv_condition = write_csv_condition

    def execute(self) -> None:
        self.csv_repository.write(self.write_csv_condition)
