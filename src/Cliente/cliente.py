from typing     import List, Optional
from decimal    import Decimal
from ..Pessoa   import Pessoa
from ..Contato  import Contato
from ..Veiculos import Veiculos

class Clientes(Pessoa):
    
    def __init__(self, nome: str, idade: int, contato: Contato, credito: Decimal, veiculos: Optional[List[Veiculos]] = None):
        super().__init__(nome, idade)
        
        self.contato  = contato
        self.credito  = credito
        self.veiculos = veiculos if veiculos is not None else []
    
    def contatos_vinculados(self):
        print(f'Contatos do cliente "{self.nome}":')
        self.contato.contatos_vinculados()

    def veiculos_vinculados(self):
        if self.veiculos:
            print(f'Veículos vinculados ao cliente "{self.nome}":')
            for v in self.veiculos:
                v.exibir_informacoes()
        else:
            print('Nenhum veiculo vinculado!')
            
    def comprar_veiculo(self, veiculo: Veiculos):
        self.veiculos.append(veiculo)