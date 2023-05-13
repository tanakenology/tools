from common_io.domain import ReadJsonlinesCondition, RowGenerator
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
