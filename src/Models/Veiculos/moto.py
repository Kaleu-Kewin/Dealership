from .veiculos import Veiculos
from src.Enum  import TipoVeiculo

class Moto(Veiculos):
    def __init__(self, modelo, marca, ano, preco, cor, quantidade, placa):
        super().__init__(modelo, marca, ano, preco, cor, quantidade, placa, TipoVeiculo.MOTO)