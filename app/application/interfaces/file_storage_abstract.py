from abc import ABC, abstractmethod

from app.application.interfaces.dtos.list_files_dto import ListFilesDto


class FileStorageAbstract(ABC):
    @abstractmethod
    def list_files(self, folder_id: str | None = None) -> ListFilesDto:
        pass

    @abstractmethod
    def upload(self, file_path: str, folder_id: str | None = None) -> str | None:
        pass

    @abstractmethod
    def download(self, file_id: str, destination_path: str) -> None:
        pass

    @abstractmethod
    def delete(self, file_id: str) -> None:
        pass
