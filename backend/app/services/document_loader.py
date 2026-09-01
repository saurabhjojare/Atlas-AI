import csv
from pathlib import Path

def load_documents(file: Path) -> list[str]:
    if file.suffix == ".txt":
        return [file.read_text(encoding="utf8")]

    if file.suffix == ".csv":
        return load_csv(file)

    raise ValueError(f"Unsupported file type: {file.suffix}")


def load_csv(file: Path) -> list[str]:
    with file.open(newline="", encoding="utf8") as csv_file:
        rows = csv.DictReader(csv_file)

        return [
            " ".join(f"{key}: {value}" for key, value in row.items())
            for row in rows
        ]