from collections.abc import Generator
from unittest.mock import patch

import common_io
from common_io.domain import (
    CsvPath,
    Delimiter,
    IsRowAsList,
    ReadCsvCondition,
    RowGenerator,
)


@patch("common_io.ReadCsvUsecase")
@patch("common_io.CsvGateway")
class TestMain:
    def test_read_csv_as_json(
        self,
        CsvGateway,
        ReadCsvUsecase,
    ):
        csv_repository = CsvGateway.return_value
        read_csv_usecase = ReadCsvUsecase.return_value
        read_csv_condition = ReadCsvCondition(
            input_path=CsvPath(value="gs://somebucket/input.csv"),
            delimiter=Delimiter(value=","),
            is_row_as_list=IsRowAsList(value=False),
        )

        def _():
            yield {"a": "1", "b": "2"}
            yield {"a": "3", "b": "4"}

        read_csv_usecase.execute.return_value = RowGenerator(value=_())

        actual = common_io.read_csv("gs://somebucket/input.csv")

        assert isinstance(actual, Generator)
        actual_list = list(actual)
        CsvGateway.assert_called_once_with()
        ReadCsvUsecase.assert_called_once_with(
            csv_repository, read_csv_condition
        )
        read_csv_usecase.execute.assert_called_once_with()
        assert actual_list == [{"a": "1", "b": "2"}, {"a": "3", "b": "4"}]

    def test_read_csv_as_list(
        self,
        CsvGateway,
        ReadCsvUsecase,
    ):
        csv_repository = CsvGateway.return_value
        read_csv_usecase = ReadCsvUsecase.return_value
        read_csv_condition = ReadCsvCondition(
            input_path=CsvPath(value="gs://somebucket/input.csv"),
            delimiter=Delimiter(value=","),
            is_row_as_list=IsRowAsList(value=True),
        )

        def _():
            yield ["a", "b"]
            yield ["1", "2"]
            yield ["3", "4"]

        read_csv_usecase.execute.return_value = RowGenerator(value=_())

        actual = common_io.read_csv(
            "gs://somebucket/input.csv", row_as_list=True
        )

        assert isinstance(actual, Generator)
        actual_list = list(actual)
        CsvGateway.assert_called_once_with()
        ReadCsvUsecase.assert_called_once_with(
            csv_repository, read_csv_condition
        )
        read_csv_usecase.execute.assert_called_once_with()
        assert actual_list == [["a", "b"], ["1", "2"], ["3", "4"]]
