import abc

from common_io.domain import ReadCsvCondition, RowGenerator


class CsvPort(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self, read_csv_condition: ReadCsvCondition) -> RowGenerator:
        raise NotImplementedError
