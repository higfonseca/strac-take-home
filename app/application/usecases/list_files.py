from app.application.interfaces.dtos.list_files_dto import ListFilesDto
from app.application.interfaces.file_storage_abstract import FileStorageAbstract


class ListFiles:
    def __init__(self, file_storage: FileStorageAbstract):
        self.__file_storage = file_storage

    def __call__(self, folder_id: str | None = None) -> ListFilesDto:
        return self.__file_storage.list_files(folder_id=folder_id)
