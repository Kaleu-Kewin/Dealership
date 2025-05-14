from src.utils import montar_opcoes, limpar_terminal, titulo
from .ui import Ui

class TelaVenda(Ui):
    def exibir(self):
        limpar_terminal()

        titulo('Tela de Vendas')

        opcao = montar_opcoes(
            "1. Realizar Venda",
            "2. Editar Venda",
            "3. Excluir Venda",
            "4. Voltar ao Menu Principal"
        )

        limpar_terminal()

        match opcao:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                print("Voltando ao Menu Principal...")
                return
