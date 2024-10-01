from unittest import TestCase
from unittest.mock import patch, Mock

from app.infrastructure.clients.authentication_client import AuthenticationClient


class TestAuthenticationClient(TestCase):
    def setUp(self):
        self.__client = AuthenticationClient()
        self.__app_flow_mock = Mock()
        self.__creds_mock = Mock()

    @patch("os.path.exists")
    @patch("app.infrastructure.clients.authentication_client.Credentials")
    def test_authenticate_WHEN_token_file_exists_THEN_calls_expected_methods(
        self, credentials_mock, exists_mock
    ):
        exists_mock.return_value = True
        self.__client.authenticate()
        credentials_mock.from_authorized_user_file.assert_called_once()

    @patch("os.path.exists")
    @patch("app.infrastructure.clients.authentication_client.open")
    @patch("app.infrastructure.clients.authentication_client.InstalledAppFlow")
    def test_authenticate_WHEN_token_file_not_exists_THEN_calls_expected_methods(
        self, appflow_mock, _, exists_mock
    ):
        exists_mock.return_value = False
        appflow_mock.from_client_secrets_file.return_value = self.__app_flow_mock

        self.__client.authenticate()

        appflow_mock.from_client_secrets_file.assert_called_once()
        self.__app_flow_mock.run_local_server.assert_called_once()

    @patch("os.path.exists")
    @patch("app.infrastructure.clients.authentication_client.Credentials")
    @patch("app.infrastructure.clients.authentication_client.open")
    def test_authenticate_WHEN_credentials_expired_THEN_calls_expected_methods(
        self, _, credentials_mock, exists_mock
    ):
        exists_mock.return_value = True
        self.__creds_mock.valid = False
        self.__creds_mock.expired = True
        self.__creds_mock.refresh_token = "refresh"
        credentials_mock.from_authorized_user_file.return_value = self.__creds_mock

        self.__client.authenticate()

        self.__creds_mock.refresh.assert_called_once()
