import io
import logging

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload

from app.application.interfaces.dtos.list_files_dto import ListFilesDto
from app.application.interfaces.file_storage_abstract import FileStorageAbstract


class GoogleDriveClient(FileStorageAbstract):
    def __init__(self, credentials: Credentials):
        self.__gdrive = build("drive", "v3", credentials=credentials)

    def list_files(self, folder_id: str | None = None) -> ListFilesDto:
        try:
            query = f"'{folder_id}' in parents" if folder_id else None

            results = (
                self.__gdrive.files()
                .list(
                    q=query,
                    fields="files(id, name)",
                )
                .execute()
            )
            items = results.get("files", [])

            files = {}
            for item in items:
                files[item["id"]] = item["name"]

            return ListFilesDto(files=files)

        except HttpError as error:
            logging.error(f"An error occurred listing GDrive files: {error}")

    def upload(self, file_path: str, folder_id: str | None = None) -> str | None:
        def get_file_name_from_path() -> str:
            spl = file_path.split("/")
            return spl[-1]

        try:
            file_metadata = {"name": get_file_name_from_path()}

            if folder_id:
                file_metadata["parents"] = [folder_id]

            media = MediaFileUpload(file_path)
            file = (
                self.__gdrive.files()
                .create(body=file_metadata, media_body=media, fields="id")
                .execute()
            )

        except HttpError as error:
            print(f"An error occurred: {error}")
            file = None

        return file.get("id")

    def download(self, file_id: str, destination_path: str) -> None:
        try:
            request = self.__gdrive.files().get_media(fileId=file_id)
            with io.FileIO(destination_path, "wb") as fh:
                downloader = MediaIoBaseDownload(fh, request)
                done = False
                while not done:
                    status, done = downloader.next_chunk()

        except HttpError as error:
            print(f"An error occurred: {error}")

    def delete(self, file_id: str) -> None:
        try:
            response = self.__gdrive.files().delete(fileId=file_id).execute()
            print(response)

        except HttpError as error:
            print(f"An error occurred: {error}")
