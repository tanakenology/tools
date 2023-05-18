import abc

from common_io.domain import (
    ReadJsonlinesCondition,
    RowGenerator,
    WriteJsonlinesCondition,
)


class JsonlinesPort(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(
        self, read_jsonlines_condition: ReadJsonlinesCondition
    ) -> RowGenerator:
        raise NotImplementedError

    @abc.abstractmethod
    def write(
        self, write_jsonlines_condition: WriteJsonlinesCondition
    ) -> None:
        raise NotImplementedError
