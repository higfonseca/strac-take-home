from dataclasses import dataclass


@dataclass
class ListFilesDto:
    files: dict[str, str]
