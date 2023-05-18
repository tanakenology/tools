from common_io.domain import (
    ReadJsonlinesCondition,
    RowGenerator,
    WriteJsonlinesCondition,
)
from common_io.driver.jsonlines_driver import JsonlinesDriver
from common_io.port.jsonlines_port import JsonlinesPort


class JsonlinesGateway(JsonlinesPort):
    def read(
        self, read_jsonlines_condition: ReadJsonlinesCondition
    ) -> RowGenerator:
        return RowGenerator(
            value=JsonlinesDriver.read(
                read_jsonlines_condition.input_path.value
            )
        )

    def write(
        self, write_jsonlines_condition: WriteJsonlinesCondition
    ) -> None:
        JsonlinesDriver.write(
            write_jsonlines_condition.output_path.value,
            write_jsonlines_condition.iterable,
        )
