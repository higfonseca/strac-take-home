from typing import Annotated

import typer
from rich import print
from rich.console import Console
from rich.table import Table

from app.infrastructure.container import ApplicationContainer

app = typer.Typer()
container = ApplicationContainer()


@app.command("list", help="List files from your Drive")
def list_files(
    folder_id: Annotated[
        str | None,
        typer.Option(
            help="Google Drive's folder_id where you want to list the files (if empty will use your Drive's root folder)",
            show_default=False,
        ),
    ] = None
) -> None:
    items = container.list_files(folder_id)
    table = Table("File ID", "Name")

    for file_id, file_name in items.files.items():
        table.add_row(file_id, file_name)

    Console().print(table)


@app.command(help="Upload a file to your Drive")
def upload(
    local_file_path: Annotated[
        str, typer.Argument(help="Local path of the file that will be uploaded")
    ],
    folder_id: Annotated[
        str | None,
        typer.Option(
            help="Google Drive's folder_id where you want to upload the file (if empty will use your Drive's root folder)",
            show_default=False,
        ),
    ] = None,
):
    file_id = container.upload_file(file_path=local_file_path, folder_id=folder_id)
    print(
        f":white_heavy_check_mark:  File uploaded to your Drive. File id: [bold]{file_id}[/bold]"
    )


@app.command(help="Download a file from your Drive")
def download(
    file_id: Annotated[
        str,
        typer.Argument(
            help="Google Drive's file id to be downloaded",
            show_default=False,
        ),
    ],
    destination_path: Annotated[
        str,
        typer.Argument(
            help="Local path where you want to save the downloaded file (with the file name, example: /usr/default/Downloads/foo.pdf)",
            show_default=False,
        ),
    ],
):
    container.download_file(file_id=file_id, destination_path=destination_path)
    print(
        f":white_heavy_check_mark:  File downloaded to directory [bold]{destination_path}[/bold]"
    )


@app.command(help="Delete a file from your Drive")
def delete(
    file_id: Annotated[
        str,
        typer.Argument(
            help="Google Drive's file id to be deleted",
            show_default=False,
        ),
    ]
):
    container.delete_file(file_id)
    print(f":white_heavy_check_mark:  Successfully deleted file [bold]{file_id}[/bold]")


@app.command(help="Remove your authentication token")
def logout():
    container.authentication_service.logout()
    print(":white_heavy_check_mark: Authentication token removed. See you soon!")
