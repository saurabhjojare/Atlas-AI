import pandas as pd
from app.repositories.base_repository import BaseRepository

class CsvRepository(BaseRepository):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_documents(self):

        df = pd.read_csv(self.file_path)

        docs = []

        for _, row in df.iterrows():
            docs.append(" | ".join(row.astype(str)))

        return docs