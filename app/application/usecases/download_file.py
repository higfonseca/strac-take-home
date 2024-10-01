from app.application.interfaces.file_storage_abstract import FileStorageAbstract


class DownloadFile:
    def __init__(self, file_storage: FileStorageAbstract):
        self.__file_storage = file_storage

    def __call__(self, file_id: str, destination_path: str) -> None:
        return self.__file_storage.download(
            file_id=file_id, destination_path=destination_path
        )
