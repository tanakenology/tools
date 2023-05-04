import abc

from common_io.domain import ReadCsvCondition, RowGenerator, WriteCsvCondition


class CsvPort(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self, read_csv_condition: ReadCsvCondition) -> RowGenerator:
        raise NotImplementedError

    @abc.abstractmethod
    def write(self, write_csv_condition: WriteCsvCondition) -> None:
        raise NotImplementedError
