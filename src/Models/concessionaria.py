from .veiculos import Veiculos
from .cliente  import Clientes

class Concessionaria:
    def __init__(self, nome: str):
        self.nome = nome
        self.estoque = []

    def adicionar_veiculo(self, veiculo: Veiculos):
        print(f'O "{veiculo.modelo}" foi adicionado a concessionaria "{self.nome}"!')
        self.estoque.append(veiculo)

    def vender_veiculo(self, veiculo: Veiculos, cliente: Clientes):
        if veiculo not in self.estoque:
            print('O Veiculo não está disponivel!')
            return

        if cliente.credito < veiculo.preco:
            print(f'O Cliente "{cliente.nome}" não possui Crédito suficiente!')
            return

        cliente.credito = cliente.credito - veiculo.preco
        cliente.comprar_veiculo(veiculo)
        self.estoque.remove(veiculo)
        print(f'O "{veiculo.modelo}" foi vendido para o cliente "{cliente.nome}"!')

    def veiculos_em_estoque(self):
        print(f'Veiculos em estoque: {len(self.estoque)}')
        for e in self.estoque:
            print(f'- {e.modelo}')
