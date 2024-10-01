import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from app.application.interfaces.authentication_abstract import AuthenticationAbstract


class AuthenticationClient(AuthenticationAbstract):
    def __init__(self):
        self.__scopes = ["https://www.googleapis.com/auth/drive"]
        self.__credentials_path = "./storage/credentials.json"
        self.__token_path = "./storage/token.json"

    def authenticate(self) -> Credentials:
        creds = None
        if os.path.exists(self.__token_path):
            creds = Credentials.from_authorized_user_file(
                self.__token_path, self.__scopes
            )

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.__credentials_path, self.__scopes
                )
                creds = flow.run_local_server(port=0)

            with open(self.__token_path, "w") as token:
                token.write(creds.to_json())

        return creds
