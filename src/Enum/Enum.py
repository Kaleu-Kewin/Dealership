from enum import Enum

class Cores(Enum):
    Preto    = 'Preto'
    Prata    = 'Prata'
    Branco   = 'Branco'
    Vermelho = 'Vermelho'
    Cinxa    = 'Cinza'

    def __str__(self) -> str:
        return self.value