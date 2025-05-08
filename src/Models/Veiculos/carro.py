from src.Enum  import Cores
from decimal   import Decimal
from .veiculos import Veiculos

class Carro(Veiculos):
    def __init__(self, modelo: str, marca: str, ano: int, cor: Cores, preco: Decimal):
        super().__init__(modelo, marca, ano, cor, preco)
    
    def exibir_informacoes(self):
        print('Informações do Veiculo: ')
        print(f'- Modelo: {self.modelo}')
        print(f'- Marca: {self.marca}')
        print(f'- Ano: {self.ano}')
        print(f'- Cor: {self.cor}')
        print(f'- Preço: R${self.preco}')