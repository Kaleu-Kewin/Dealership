from decimal   import Decimal
from .veiculos import Veiculos

class Carro(Veiculos):
    
    def __init__(self, modelo: str, marca: str, ano: str, cor: str, preco: Decimal):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.preco = preco
    
    def exibir_informacoes(self):
        print('Informações do Veiculo: ')
        print(f'- Modelo: {self.modelo}')
        print(f'- Marca: {self.marca}')
        print(f'- Ano: {self.ano}')
        print(f'- Cor: {self.cor}')
        print(f'- Preço: R${self.preco}')