from unittest import TestCase
from unittest.mock import Mock

from app.application.usecases.download_file import DownloadFile


class TestDownloadFile(TestCase):
    def setUp(self):
        self.storage = Mock()
        self.use_case = DownloadFile(self.storage)

    def test_download_file_WHEN_called_THEN_calls_file_storage_client(self):
        file_id = "foo"
        destination_path = "/foo/bar.txt"
        self.use_case(file_id, destination_path)
        self.storage.download.assert_called_with(
            file_id=file_id, destination_path=destination_path
        )
