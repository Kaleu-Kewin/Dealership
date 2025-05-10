from ..Utils import montar_opcoes, limpar_terminal, titulo
from .ui     import Ui

class TelaVeiculo(Ui):
    def exibir(self):
        limpar_terminal()
        
        titulo('Tela de Veiculos')
        
        opcao = montar_opcoes(
            "1. Cadastrar Veiculo",
            "2. Listar Veiculos",
            "3. Editar Veiculo",
            "4. Excluir Veiculo",
            "5. Voltar ao Menu Principal"
        )
        
        limpar_terminal()
        
        match opcao:
            case 1:
                self.cadastrar_veiculo()
            case 2:
                self.listar_veiculos()
            case 3:
                self.editar_veiculo()
            case 4:
                self.excluir_veiculo()
            case 5:
                print("Voltando ao Menu Principal...")
                return