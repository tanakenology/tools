from unittest import TestCase
from unittest.mock import MagicMock

from common_io.usecase.read_jsonlines import (JsonlinesPort,
                                              ReadJsonlinesCondition,
                                              ReadJsonlinesUsecase)


class ReadJsonlinesUsecaseTestCase(TestCase):
    def test_execute(self):
        jsonlines_repository = MagicMock(spec=JsonlinesPort)
        read_jsonlines_condition = MagicMock(spec=ReadJsonlinesCondition)
        expected = jsonlines_repository.read.return_value

        sut = ReadJsonlinesUsecase(
            jsonlines_repository, read_jsonlines_condition
        )
        actual = sut.execute()

        jsonlines_repository.read.assert_called_once_with(
            read_jsonlines_condition
        )
        self.assertEqual(actual, expected)
