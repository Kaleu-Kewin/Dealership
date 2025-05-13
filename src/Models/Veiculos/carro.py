from src.Enum  import TipoVeiculo as t
from .veiculos import Veiculos, VeiculosDAO

class Carro(Veiculos):
    def __init__(self, modelo, marca, ano, preco, cor, quantidade, placa):
        super().__init__(modelo, marca, ano, preco, cor, quantidade, placa, str(t.CARRO))

    def cadastrar(self):
        carro = VeiculosDAO(self)
        carro.cadastrar_veiculo()
