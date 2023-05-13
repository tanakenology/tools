import abc

from common_io.domain import ReadJsonlinesCondition, RowGenerator


class JsonlinesPort(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(
        self, read_jsonlines_condition: ReadJsonlinesCondition
    ) -> RowGenerator:
        raise NotImplementedError
