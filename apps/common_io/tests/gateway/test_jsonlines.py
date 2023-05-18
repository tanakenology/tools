from unittest import TestCase
from unittest.mock import MagicMock, patch

from common_io.domain import (
    JsonlinesPath,
    ReadJsonlinesCondition,
    WriteJsonlinesCondition,
    RowGenerator,
    Iterable,
)
from common_io.gateway.jsonlines_gateway import JsonlinesGateway


@patch("common_io.gateway.jsonlines_gateway.JsonlinesDriver")
class JsonlinesGatewayTestCase(TestCase):
    def test_read(self, JsonlinesDriver):
        def _():
            yield {"a": 1, "b": 2}

        JsonlinesDriver.read.return_value = _()
        expected = RowGenerator(value=_())

        sut = JsonlinesGateway()
        actual = sut.read(
            ReadJsonlinesCondition(
                input_path=JsonlinesPath(value="gs://somebucket/input.jsonl")
            )
        )

        JsonlinesDriver.read.assert_called_once_with(
            "gs://somebucket/input.jsonl"
        )
        self.assertEqual(list(actual.value), list(expected.value))

    def test_write(self, JsonlinesDriver):
        output = MagicMock(spec=Iterable)

        sut = JsonlinesGateway()
        sut.write(
            WriteJsonlinesCondition(
                output_path=JsonlinesPath(
                    value="gs://somebucket/output.jsonl"
                ),
                iterable=output,
            )
        )

        JsonlinesDriver.write.assert_called_once_with(
            "gs://somebucket/output.jsonl",
            output,
        )
