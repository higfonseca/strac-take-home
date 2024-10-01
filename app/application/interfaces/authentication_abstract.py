from abc import ABC, abstractmethod

from google.oauth2.credentials import Credentials


class AuthenticationAbstract(ABC):
    @abstractmethod
    def authenticate(self) -> Credentials:
        pass
