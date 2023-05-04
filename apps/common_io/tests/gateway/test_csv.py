from unittest import TestCase
from unittest.mock import MagicMock, patch

from common_io.domain import CsvPath, Delimiter, IsRowAsList, Iterable
from common_io.gateway.csv_gateway import (
    CsvGateway,
    ReadCsvCondition,
    RowGenerator,
    WriteCsvCondition,
)


@patch("common_io.gateway.csv_gateway.CsvDriver")
class CsvGatewayTestCase(TestCase):
    def test_read(self, CsvDriver):
        def _():
            yield {"a": 1, "b": 2}

        CsvDriver.read.return_value = _()
        expected = RowGenerator(value=_())

        sut = CsvGateway()
        actual = sut.read(
            ReadCsvCondition(
                input_path=CsvPath(value="gs://somebucket/input.csv"),
                delimiter=Delimiter(value=","),
                is_row_as_list=IsRowAsList(value=False),
            )
        )

        CsvDriver.read.assert_called_once_with(
            "gs://somebucket/input.csv",
            delimiter=",",
            row_as_list=False,
        )
        self.assertEqual(list(actual.value), list(expected.value))

    def test_write(self, CsvDriver):
        output = MagicMock(spec=Iterable)

        sut = CsvGateway()
        sut.write(
            WriteCsvCondition(
                output_path=CsvPath(value="gs://somebucket/output.csv"),
                iterable=output,
                delimiter=Delimiter(value=","),
            )
        )

        CsvDriver.write.assert_called_once_with(
            "gs://somebucket/output.csv",
            output,
            delimiter=",",
        )
