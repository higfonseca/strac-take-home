from unittest import TestCase
from unittest.mock import Mock, patch

from google.oauth2.credentials import Credentials

from app.application.interfaces.authentication_abstract import AuthenticationAbstract
from app.application.services.authentication_service import AuthenticationService


class TestAuthenticationService(TestCase):
    def setUp(self):
        self.auth_client = Mock(AuthenticationAbstract)
        self.service = AuthenticationService(self.auth_client)

    def tearDown(self):
        patch.stopall()

    def test_authenticate_WHEN_called_RETURNS_credentials(self):
        creds = Credentials("token")
        self.auth_client.authenticate.return_value = creds

        result = self.service.authenticate()

        self.assertEqual(result, creds)

    def test_authenticate_WHEN_called_THEN_calls_auth_client(self):
        self.service.authenticate()
        self.auth_client.authenticate.assert_called_once()

    @patch("os.path.exists")
    @patch("os.remove")
    def test_logout_WHEN_called_and_token_file_exists_THEN_removes_it(
        self, mock_remove, mock_exists
    ):
        mock_exists.return_value = True
        self.service.logout()
        mock_remove.assert_called_once()

    @patch("os.path.exists")
    @patch("os.remove")
    def test_logout_WHEN_called_and_token_file_not_exists_THEN_do_not_call_os_remove(
        self, mock_remove, mock_exists
    ):
        mock_exists.return_value = False
        self.service.logout()
        mock_remove.assert_not_called()
