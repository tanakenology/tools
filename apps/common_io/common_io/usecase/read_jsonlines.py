from common_io.domain import ReadJsonlinesCondition
from common_io.port.jsonlines_port import JsonlinesPort


class ReadJsonlinesUsecase:
    def __init__(
            self,
            jsonlines_repository: JsonlinesPort,
            read_jsonlines_condition: ReadJsonlinesCondition,
    ):
        self.jsonlines_repository = jsonlines_repository
        self.read_jsonlines_condition = read_jsonlines_condition

    def execute(self):
        return self.jsonlines_repository.read(self.read_jsonlines_condition)
