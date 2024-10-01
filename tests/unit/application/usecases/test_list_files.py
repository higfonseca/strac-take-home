from unittest import TestCase
from unittest.mock import Mock

from app.application.usecases.list_files import ListFiles


class TestListFile(TestCase):
    def setUp(self):
        self.storage = Mock()
        self.use_case = ListFiles(self.storage)

    def test_list_files_WHEN_called_with_folder_id_THEN_calls_file_storage_client_with_folder_id(
        self,
    ):
        folder_id = "foo"
        self.use_case(folder_id)
        self.storage.list_files.assert_called_with(folder_id=folder_id)

    def test_list_files_WHEN_called_without_folder_id_THEN_calls_file_storage_client_with_folder_id_none(
        self,
    ):
        self.use_case()
        self.storage.list_files.assert_called_with(folder_id=None)
