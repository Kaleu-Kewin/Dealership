from abc      import ABC, abstractmethod
from src.Enum import Cores, TipoVeiculo
from decimal  import Decimal

class Veiculos(ABC):
    def __init__(self, modelo: str, marca: str, ano: int, preco: Decimal, cor: Cores, quantidade: int, placa: str, tipo_veiculo: TipoVeiculo):
        self.modelo       = modelo
        self.marca        = marca
        self.ano          = ano
        self.preco        = Decimal(preco)
        self.cor          = cor
        self.quantidade   = quantidade
        self.placa        = placa
        self.tipo_veiculo = tipo_veiculo