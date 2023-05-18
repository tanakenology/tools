from common_io.port.jsonlines_port import JsonlinesPort
from common_io.domain import WriteJsonlinesCondition


class WriteJsonlinesUsecase:
    def __init__(
        self,
        jsonlines_repository: JsonlinesPort,
        write_jsonlines_condition: WriteJsonlinesCondition,
    ):
        self.jsonlines_repository = jsonlines_repository
        self.write_jsonlines_condition = write_jsonlines_condition

    def execute(self):
        self.jsonlines_repository.write(self.write_jsonlines_condition)
