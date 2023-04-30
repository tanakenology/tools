from unittest import TestCase
from unittest.mock import MagicMock

from common_io.usecase.read_csv import (
    CsvPath,
    CsvPort,
    Delimiter,
    IsRowAsList,
    ReadCsvCondition,
    ReadCsvUsecase,
)


class ReadCsvUsecaseTestCase(TestCase):
    def test_execute(self):
        csv_repository = MagicMock(spec=CsvPort)
        read_csv_condition = ReadCsvCondition(
            input_path=CsvPath(value="gs://somebucket/input.csv"),
            delimiter=Delimiter(value=","),
            is_row_as_list=IsRowAsList(value=False),
        )
        expected = csv_repository.read.return_value

        sut = ReadCsvUsecase(csv_repository, read_csv_condition)
        actual = sut.execute()

        csv_repository.read.assert_called_once_with(read_csv_condition)
        self.assertEqual(actual, expected)
