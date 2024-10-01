from app.application.interfaces.file_storage_abstract import FileStorageAbstract


class DeleteFile:
    def __init__(self, file_storage: FileStorageAbstract):
        self.__file_storage = file_storage

    def __call__(self, file_id: str) -> None:
        self.__file_storage.delete(file_id)
