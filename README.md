# Strac Take-Home Test
This is a CLI application to deal with Google Drive files (list, download, upload, delete).

[![codecov](https://codecov.io/gh/higfonseca/strac-take-home/graph/badge.svg?token=JBXSU3XUG4)](https://codecov.io/gh/higfonseca/strac-take-home)

## Requirements

- Python >= 3.10
- [pip](https://pypi.org/project/pip/)

## Installation
- Setup an application in [Google Cloud](https://developers.google.com/identity/protocols/oauth2/service-account#creatinganaccount)
- Create a `storage` directory inside project's root folder
- Download the `credentials.json` from Google Cloud and place it in the `storage` directory
- In your terminal, inside project's root, create a Virtual Environment, activate it and install project's dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Instructions
To run the application, type the following command in your terminal:
```bash
python3 -m app.main --help
```

This will list all available commands:
```
╭─ Commands ───────────────────────────────────╮
│ delete     Delete a file from your Drive     | 
│ download   Download a file from your Drive   │
│ list       List files from your Drive        │
│ logout     Remove your authentication token  │
│ upload     Upload a file to your Drive       │
╰──────────────────────────────────────────────╯
```

To know more about the `list` command and its required or optional arguments, try:
```bash
python3 -m app.main list --help
```

## Run tests

In project's root dir, run:
```bash
python3 -m unittest
```

## Decisions Breakdown

- Why a CLI: due to the time constraint I wanted an interface that would be quick to develop and test. With Python's [Typer lib](https://typer.tiangolo.com/) this process gets intuitive.
- Software Architecture: the idea was to separate concerns into layers of responsibility. Checking the `app` dir you will notice that the application was split into `application` (application rules), `infrastructure` (external calls to services), and finally `presentation` (entry/exit point for user's inputs)
- Dependency Injection: inside the `ApplicationContainer` you will find a basic dependency injection setup. The main goals were to attend to SOLID's DIP principle and also ease the testing process by allowing mocks to be injected in the desired classes
- Router: you will notice that the `Router` file is the only one using a procedural approach. It had to be this way due to limitations with `Typer`
- Tests: as mentioned, due to the time constraint, I left some "unhappy" paths untested (especially if any call to the GoogleClient fails)
- CI: I added a simple Github Actions script to validate the tests before the merge to the main branch