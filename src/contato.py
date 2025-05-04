from typing import List

class Contato:
    def __init__(self, contatos: List[str]):
        self._contatos = contatos
                   
    def contatos_vinculados(self):      
        for c in self._contatos:
            print(f'- {c}')