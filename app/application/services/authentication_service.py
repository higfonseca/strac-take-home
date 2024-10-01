import os

from google.oauth2.credentials import Credentials

from app.application.interfaces.authentication_abstract import AuthenticationAbstract


class AuthenticationService:
    def __init__(self, authentication: AuthenticationAbstract):
        self.__authentication = authentication

    def authenticate(self) -> Credentials:
        return self.__authentication.authenticate()

    @staticmethod
    def logout() -> None:
        if os.path.exists("storage/token.json"):
            os.remove("storage/token.json")
