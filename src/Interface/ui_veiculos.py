from src.Utils  import *
from .ui        import Ui
from src.Models import Carro, Moto
from src.Enum   import TipoVeiculo as v, Cores as c

class TelaVeiculo(Ui):
    def __init__(self):
        self.classes = {
            v.CARRO : Carro,
            v.MOTO  : Moto
        }

    def obter_veiculo(self, dados: dict):
        return self.classes.get(dados['tipo_veiculo'])

    def cadastrar_veiculo(self):
        titulo('Insira as informações do Veiculo')

        respostas = [
            perguntar('Modelo'),
            perguntar('Marca'),
            perguntar('Ano'),
            perguntar('Preço'),
            selecionar('Cor', [c.Preto.value, c.Branco.value, c.Vermelho.value, c.Prata.value]),
            perguntar('Placa'),
            perguntar('Quantidade'),
            selecionar('Tipo de Veiculo', [v.CARRO, v.MOTO])
        ]

        dados = {
            'modelo'       : respostas[0],
            'marca'        : respostas[1],
            'ano'          : respostas[2],
            'preco'        : validar_preco(respostas[3]),
            'cor'          : respostas[4],
            'quantidade'   : respostas[6],
            'placa'        : respostas[5],
            'tipo_veiculo' : respostas[7]
        }

        classe  = self.obter_veiculo(dados)
        veiculo = classe(
            dados['modelo'],
            dados['marca'],
            dados['ano'],
            dados['preco'],
            dados['cor'],
            dados['quantidade'],
            dados['placa']
        )
        veiculo.cadastrar()
        pressione_enter()

    def listar_veiculos(self):
        pass

    def editar_veiculo(self):
        pass

    def excluir_veiculo(self):
        pass

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
