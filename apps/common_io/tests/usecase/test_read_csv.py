from unittest import TestCase
from unittest.mock import MagicMock

from common_io.usecase.read_csv import (CsvPort, ReadCsvCondition,
                                        ReadCsvUsecase)


class ReadCsvUsecaseTestCase(TestCase):
    def test_execute(self):
        csv_repository = MagicMock(spec=CsvPort)
        read_csv_condition = MagicMock(spec=ReadCsvCondition)
        expected = csv_repository.read.return_value

        sut = ReadCsvUsecase(csv_repository, read_csv_condition)
        actual = sut.execute()

        csv_repository.read.assert_called_once_with(read_csv_condition)
        self.assertEqual(actual, expected)
