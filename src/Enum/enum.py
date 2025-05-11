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
    ATIVO   = 'ATIVO'
    INATIVO = 'INATIVO'

    def __str__(self) -> str:
        return self.value
    
class TipoVeiculo(Enum):
    CARRO = 'CARRO'
    MOTO  = 'MOTO' 