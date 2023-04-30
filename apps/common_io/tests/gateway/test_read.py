from unittest import TestCase
from unittest.mock import patch

from common_io.gateway.csv_gateway import (
    CsvGateway,
    CsvPath,
    Delimiter,
    IsRowAsList,
    ReadCsvCondition,
    RowGenerator,
)


class CsvGatewayTestCase(TestCase):
    @patch("common_io.gateway.csv_gateway.CsvDriver")
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
