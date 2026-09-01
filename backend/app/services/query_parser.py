import re
from datetime import datetime


def parse_query(message: str) -> dict | None:
    match = re.search(
        r"\b(january|february|march|april|may|june|july|august|"
        r"september|october|november|december)\s+(\d{4})\b",
        message.lower(),
    )

    if not match:
        return None

    month = datetime.strptime(match.group(1), "%B").month
    year = int(match.group(2))

    return {
        "year": year,
        "month": month,
    }