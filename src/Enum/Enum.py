from enum import Enum

class Cores(Enum):
    Preto    = 'Preto'
    Prata    = 'Prata'
    Branco   = 'Branco'
    Vermelho = 'Vermelho'
    Cinxa    = 'Cinza'

    def __str__(self) -> str:
        return self.value
    
class Status(Enum):
    Ativo   = 'Ativo'
    Inativo = 'Inativo'

    def __str__(self) -> str:
        return self.value