from src.Enum  import TipoVeiculo as t
from .veiculos import Veiculos, VeiculosDAO

class Moto(Veiculos):
    def __init__(self, modelo, marca, ano, preco, cor, quantidade, placa):
        super().__init__(modelo, marca, ano, preco, cor, quantidade, placa, str(t.MOTO))

    def cadastrar(self):
        moto = VeiculosDAO(self)
        moto.cadastrar_veiculo()
