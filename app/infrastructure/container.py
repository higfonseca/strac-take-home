from app.application.services.authentication_service import AuthenticationService
from app.application.usecases.delete_file import DeleteFile
from app.application.usecases.download_file import DownloadFile
from app.application.usecases.list_files import ListFiles
from app.application.usecases.upload_file import UploadFile
from app.infrastructure.clients.authentication_client import AuthenticationClient
from app.infrastructure.clients.google_drive_client import GoogleDriveClient


# DEPENDENCY INJECTION MANAGEMENT
class ApplicationContainer:
    # SETTING VARIABLES WITH DOUBLE UNDERSCORE FOR PRIVATE ACCESS
    # AS A CONVENTION, SINCE PYTHON DOES NOT HAVE ACCESS MODIFIERS

    __authentication_client = AuthenticationClient()
    authentication_service = AuthenticationService(__authentication_client)
    __creds = authentication_service.authenticate()
    file_storage_client = GoogleDriveClient(__creds)

    # USE CASES
    list_files = ListFiles(file_storage_client)
    download_file = DownloadFile(file_storage_client)
    upload_file = UploadFile(file_storage_client)
    delete_file = DeleteFile(file_storage_client)
