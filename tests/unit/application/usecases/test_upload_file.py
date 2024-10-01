from unittest import TestCase
from unittest.mock import Mock

from app.application.usecases.upload_file import UploadFile


class TestDownloadFile(TestCase):
    def setUp(self):
        self.storage = Mock()
        self.use_case = UploadFile(self.storage)

    def test_upload_file_WHEN_called_with_folder_id_THEN_calls_file_storage_client(
        self,
    ):
        folder_id = "foo"
        file_path = "/foo/bar.txt"
        self.use_case(file_path=file_path, folder_id=folder_id)
        self.storage.upload.assert_called_with(file_path=file_path, folder_id=folder_id)

    def test_upload_file_WHEN_called_without_folder_id_THEN_calls_file_storage_client_with_folder_id_none(
        self,
    ):
        file_path = "/foo/bar.txt"
        self.use_case(file_path=file_path)
        self.storage.upload.assert_called_with(file_path=file_path, folder_id=None)
