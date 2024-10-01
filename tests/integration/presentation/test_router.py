from unittest import TestCase
from unittest.mock import patch, Mock

from typer.testing import CliRunner

from app.application.interfaces.dtos.list_files_dto import ListFilesDto

runner = CliRunner()


class TestRouter(TestCase):
    def tearDown(self):
        patch.stopall()

    def test_list_WHEN_called_RETURNS_files_list(self):
        list_files_mock = ListFilesDto(files={"id1": "file1", "id2": "file2"})

        with patch(
            "app.application.services.authentication_service.AuthenticationService"
        ) as auth_service_mock:
            with patch(
                "app.infrastructure.clients.google_drive_client.GoogleDriveClient.list_files"
            ) as gdrive_list_mock:
                auth_service_mock.return_value = Mock()
                gdrive_list_mock.return_value = list_files_mock

                from app.presentation.router import app

                result = runner.invoke(app, ["list"])

                self.assertEqual(result.exit_code, 0)
                self.assertTrue("id1" in result.stdout)
                self.assertTrue(list_files_mock.files["id1"] in result.stdout)
                self.assertTrue("id2" in result.stdout)
                self.assertTrue(list_files_mock.files["id2"] in result.stdout)

    def test_upload_WHEN_called_THEN_calls_google_drive_client_upload_method(self):
        file_path = "/foo/bar/shu.docx"
        folder_id = "id1"

        with patch(
            "app.application.services.authentication_service.AuthenticationService"
        ) as auth_service_mock:
            with patch(
                "app.infrastructure.clients.google_drive_client.GoogleDriveClient.upload"
            ) as gdrive_upload_mock:
                auth_service_mock.return_value = Mock()

                from app.presentation.router import app

                result = runner.invoke(
                    app, ["upload", file_path, "--folder-id", folder_id]
                )

                gdrive_upload_mock.assert_called_once_with(
                    file_path=file_path, folder_id=folder_id
                )

                self.assertEqual(result.exit_code, 0)
                self.assertTrue("File uploaded to your Drive" in result.stdout)

    def test_download_WHEN_called_THEN_calls_google_drive_client_download_method(self):
        download_path = "/foo/bar/shu.docx"
        file_id = "id1"

        with patch(
            "app.application.services.authentication_service.AuthenticationService"
        ) as auth_service_mock:
            with patch(
                "app.infrastructure.clients.google_drive_client.GoogleDriveClient.download"
            ) as gdrive_download_mock:
                auth_service_mock.return_value = Mock()

                from app.presentation.router import app

                result = runner.invoke(app, ["download", file_id, download_path])

                gdrive_download_mock.assert_called_once_with(
                    file_id=file_id, destination_path=download_path
                )

                self.assertEqual(result.exit_code, 0)
                self.assertTrue("File downloaded to directory" in result.stdout)

    def test_delete_WHEN_called_THEN_calls_google_drive_client_delete_method(self):
        file_id = "id1"

        with patch(
            "app.application.services.authentication_service.AuthenticationService"
        ) as auth_service_mock:
            with patch(
                "app.infrastructure.clients.google_drive_client.GoogleDriveClient.delete"
            ) as gdrive_delete_mock:
                auth_service_mock.return_value = Mock()

                from app.presentation.router import app

                result = runner.invoke(app, ["delete", file_id])

                gdrive_delete_mock.assert_called_once_with(file_id)

                self.assertEqual(result.exit_code, 0)
                self.assertTrue("Successfully deleted file" in result.stdout)

    def test_logout_WHEN_called_THEN_calls_authentication_service_logout_method(self):
        with patch(
            "app.application.services.authentication_service.AuthenticationService"
        ) as auth_service_mock:
            from app.presentation.router import app

            result = runner.invoke(app, ["logout"])

            self.assertEqual(result.exit_code, 0)
            self.assertTrue("Authentication token removed" in result.stdout)
