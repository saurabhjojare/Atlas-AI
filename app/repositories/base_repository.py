from abc import ABC, abstractmethod

class BaseRepository(ABC):

    @abstractmethod
    def load_documents(self):
        pass