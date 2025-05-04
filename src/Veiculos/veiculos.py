from abc     import ABC, abstractmethod
from decimal import Decimal
from ..Enum  import Cores

class Veiculos(ABC): # classe abstrata
    def __init__(self, modelo: str, marca: str, ano: int, cor: Cores, preco: Decimal):
        self.modelo = modelo
        self.marca  = marca
        self.ano    = ano
        self.cor    = cor
        self.preco  = Decimal(preco)
        
    @abstractmethod
    def exibir_informacoes(self):
        pass