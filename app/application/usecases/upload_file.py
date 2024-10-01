from app.application.interfaces.file_storage_abstract import FileStorageAbstract


class UploadFile:
    def __init__(self, file_storage: FileStorageAbstract):
        self.__file_storage = file_storage

    def __call__(self, file_path: str, folder_id: str | None = None) -> str:
        return self.__file_storage.upload(file_path=file_path, folder_id=folder_id)
