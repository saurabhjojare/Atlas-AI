import csv
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass
class Document:
    content: str
    metadata: dict


def load_documents(file: Path) -> list[Document]:
    if file.suffix == ".txt":
        return [Document(file.read_text(encoding="utf8"), {})]

    if file.suffix == ".csv":
        return load_csv(file)

    raise ValueError(f"Unsupported file type: {file.suffix}")


def load_csv(file: Path) -> list[Document]:
    with file.open(newline="", encoding="utf8") as csv_file:
        return [create_document(row) for row in csv.DictReader(csv_file)]


def create_document(row: dict) -> Document:
    return Document(
        content=" ".join(f"{key}: {value}" for key, value in row.items()),
        metadata={
            key: convert_value(value)
            for key, value in row.items()
        },
    )


def convert_value(value: str):
    try:
        return int(value)
    except ValueError:
        pass

    try:
        return float(value)
    except ValueError:
        pass

    return value