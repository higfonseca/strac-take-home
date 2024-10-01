from unittest import TestCase
from unittest.mock import Mock

from app.application.usecases.delete_file import DeleteFile


class TestDeleteFile(TestCase):
    def setUp(self):
        self.storage = Mock()
        self.use_case = DeleteFile(self.storage)

    def test_delete_file_WHEN_called_THEN_calls_file_storage_client(self):
        file_id = "foo"
        self.use_case(file_id)
        self.storage.delete.assert_called_with(file_id)
