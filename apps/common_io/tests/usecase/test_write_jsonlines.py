from unittest import TestCase
from unittest.mock import MagicMock
from common_io.usecase.write_jsonlines import (
    JsonlinesPort,
    WriteJsonlinesCondition,
    WriteJsonlinesUsecase,
)


class WriteJsonlinesUsecaseTestCase(TestCase):
    def test_execute(self):
        jsonlines_repository = MagicMock(spec=JsonlinesPort)
        write_jsonlines_condition = MagicMock(spec=WriteJsonlinesCondition)

        sut = WriteJsonlinesUsecase(
            jsonlines_repository, write_jsonlines_condition
        )
        sut.execute()

        jsonlines_repository.write.assert_called_once_with(
            write_jsonlines_condition
        )
