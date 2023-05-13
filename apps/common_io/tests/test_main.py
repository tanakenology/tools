from collections.abc import Generator
from unittest.mock import patch

import common_io
from common_io.domain import (CsvPath, Delimiter, IsRowAsList, JsonlinesPath,
                              ReadCsvCondition, ReadJsonlinesCondition,
                              RowGenerator, WriteCsvCondition)


@patch("common_io.ReadCsvUsecase")
@patch("common_io.CsvGateway")
class TestReadCsv:
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


@patch("common_io.WriteCsvUsecase")
@patch("common_io.CsvGateway")
class TestWriteCsv:
    def test_write_csv(self, CsvGateway, WriteCsvUsecase):
        csv_repository = CsvGateway.return_value
        write_csv_usecase = WriteCsvUsecase.return_value
        output = [{"a": "1", "b": "2"}, {"a": "3", "b": "4"}]
        write_csv_condition = WriteCsvCondition(
            output_path=CsvPath(value="gs://somebucket/output.csv"),
            iterable=output,
            delimiter=Delimiter(value=","),
        )

        common_io.write_csv("gs://somebucket/output.csv", output)

        CsvGateway.assert_called_once_with()
        WriteCsvUsecase.assert_called_once_with(
            csv_repository, write_csv_condition
        )
        write_csv_usecase.execute.assert_called_once_with()


@patch("common_io.ReadJsonlinesUsecase")
@patch("common_io.JsonlinesGateway")
class TestReadJsonlines:
    def test_read_jsonlines(self, JsonlinesGateway, ReadJsonlinesUsecase):
        jsonlines_repository = JsonlinesGateway.return_value
        read_jsonlines_usecase = ReadJsonlinesUsecase.return_value
        read_jsonlines_condition = ReadJsonlinesCondition(
            input_path=JsonlinesPath(value="gs://somebucket/input.jsonl")
        )

        def _():
            yield {"a": "1", "b": "2"}
            yield {"a": "3", "b": "4"}

        read_jsonlines_usecase.execute.return_value = RowGenerator(value=_())

        actual = common_io.read_jsonlines("gs://somebucket/input.jsonl")

        assert isinstance(actual, Generator)
        actual_list = list(actual)
        JsonlinesGateway.assert_called_once_with()
        ReadJsonlinesUsecase.assert_called_once_with(
            jsonlines_repository, read_jsonlines_condition
        )
        read_jsonlines_usecase.execute.assert_called_once_with()
        assert actual_list == [{"a": "1", "b": "2"}, {"a": "3", "b": "4"}]
