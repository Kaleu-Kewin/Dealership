class Pessoa: 
    
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
        
    def detalhes(self):
        print(f'Nome: {self.nome} \n Idade: {self.idade}')