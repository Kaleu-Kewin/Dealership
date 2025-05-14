from .ui_cliente  import TelaCliente
from .ui_veiculos import TelaVeiculo
from .ui_vendas   import TelaVenda
from .ui          import Ui
from src.utils    import *

class Menu(Ui):
    def __init__(self):
        pass

    def exibir(self):
        while True:
            titulo('Menu Principal')

            opcao = montar_opcoes(
                "1. Tela de Clientes.",
                "2. Tela de Veiculos.",
                "3. Tela de Vendas.",
                "4. Sair."
            )

            limpar_terminal()

            match opcao:
                case 1:
                    tela_cliente = TelaCliente()
                    tela_cliente.exibir()
                case 2:
                    tela_veiculo = TelaVeiculo()
                    tela_veiculo.exibir()
                case 3:
                    tela_venda = TelaVenda()
                    tela_venda.exibir()
                case 4:
                    print("Finalizando programa...")
                    exit()
                case _:
                    print("Opção inválida. Tente novamente.")
