from abc import ABC, abstractmethod

class Veiculos(ABC):
    
    @abstractmethod
    def exibir_informacoes(self):
        pass