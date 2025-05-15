from src.Enum  import TipoVeiculo as t
from .veiculos import Veiculos, VeiculosDAO

class Carro(Veiculos):
    def __init__(self, modelo, marca, ano, preco, cor, quantidade, placa):
        super().__init__(modelo, marca, ano, preco, cor, quantidade, placa, str(t.CARRO))
        self.carro = VeiculosDAO(self)

    def cadastrar(self):
        self.carro.cadastrar_veiculo()

    def editar(self, codigo_veiculo):
        self.carro.editar_veiculo(codigo_veiculo)
