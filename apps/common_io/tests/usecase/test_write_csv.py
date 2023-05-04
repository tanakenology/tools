from unittest import TestCase
from unittest.mock import MagicMock

from common_io.usecase.write_csv import (
    CsvPort,
    WriteCsvCondition,
    WriteCsvUsecase,
)


class WriteCsvUsecaseTestCase(TestCase):
    def test_execute(self):
        csv_repository = MagicMock(spec=CsvPort)
        write_csv_condition = MagicMock(spec=WriteCsvCondition)

        sut = WriteCsvUsecase(csv_repository, write_csv_condition)
        sut.execute()

        csv_repository.write.assert_called_once_with(write_csv_condition)
