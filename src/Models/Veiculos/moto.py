from src.enums import TipoVeiculo as t
from .veiculos import Veiculos, VeiculosDAO

class Moto(Veiculos):
    def __init__(self, modelo, marca, ano, preco, cor, quantidade, placa):
        super().__init__(modelo, marca, ano, preco, cor, quantidade, placa, str(t.MOTO))
        self.moto = VeiculosDAO(self)

    def cadastrar(self):
        self.moto.cadastrar_veiculo()

    def editar(self, codigo_veiculo):
        self.moto.editar_veiculo(codigo_veiculo)
