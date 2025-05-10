from abc import ABC, abstractmethod

class Ui(ABC):
    @abstractmethod
    def exibir(self):
        pass