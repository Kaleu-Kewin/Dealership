from src.utils  import *
from .ui        import Ui
from src.models import Carro, Moto
from src.instances.db_instance import db
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
        colunas = ['CÓDIGO', 'MODELO', 'MARCA', 'ANO', 'PREÇO', 'COR', 'QUANTIDADE', 'PLACA', 'TIPO DO VEICULO']
        indices = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        db.listar_registros('VEICULOS', colunas, indices, 'VEI_CODIGO')
        pressione_enter()

    def editar_veiculo(self):
        codigo_veiculo     = perguntar('Digite o código do veiculo que deseja alterar')
        veiculo_encontrado = db.buscar('VEICULOS', 'VEI_CODIGO', codigo_veiculo)

        titulo(f'Veiculo encontrado: {veiculo_encontrado[2]}'.upper())

        respostas = [
            perguntar(f'Modelo atual: {veiculo_encontrado[2]}\n  Novo Modelo:'),
            perguntar(f'Marca atual: {veiculo_encontrado[1]}\n  Nova Marca:'),
            perguntar(f'Ano atual: {veiculo_encontrado[3]}\n  Novo Ano:'),
            perguntar(f'Preço atual: {veiculo_encontrado[4]}\n  Novo Preço:'),
            selecionar(f'Cor atual: {veiculo_encontrado[5]}\n  Nova cor:', [c.Preto.value, c.Branco.value, c.Vermelho.value, c.Prata.value]),
            perguntar(f'Quantidade atual: {veiculo_encontrado[6]}\n  Nova Quantidade:'),
            perguntar(f'Placa atual: {veiculo_encontrado[7]}\n  Nova Placa:'),
            selecionar(f'Tipo de Veiculo atual: {veiculo_encontrado[8]}\n  Novo Tipo de Veiculo:', [v.CARRO, v.MOTO])
        ]

        dados = {
            "modelo"       : respostas[0] or veiculo_encontrado[1],
            "marca"        : respostas[1] or veiculo_encontrado[2],
            "ano"          : respostas[2] or veiculo_encontrado[3],
            "preco"        : respostas[3] or veiculo_encontrado[4],
            "cor"          : respostas[4] or veiculo_encontrado[5],
            "quantidade"   : respostas[5] or veiculo_encontrado[6],
            "placa"        : respostas[6] or veiculo_encontrado[7],
            "tipo_veiculo" : respostas[7] or veiculo_encontrado[8]
        }

        classe  = self.obter_veiculo(dados)
        veiculo = classe(
            dados["modelo"],
            dados["marca"],
            dados["ano"],
            dados["preco"],
            dados["cor"],
            dados["quantidade"],
            dados["placa"]
        )
        veiculo.editar(codigo_veiculo)
        pressione_enter()

    def excluir_veiculo(self):
        codigo_veiculo     = perguntar('Digite o código do veiculo que deseja excluir')
        veiculo_encontrado = db.buscar('VEICULOS', 'VEI_CODIGO', codigo_veiculo)

        if veiculo_encontrado:
            titulo(f'Veiculo encontrado: {veiculo_encontrado[1]}'.upper())
            resposta = selecionar('Tem certeza que deseja excluir?', ['SIM', 'NÃO']).strip().lower()

            if resposta and resposta[0] == 's':
                db.excluir_por_id('VEICULOS', 'VEI_CODIGO', codigo_veiculo)
            else:
                print('\nExclusão cancelada.')
        else:
            print('\nVeiculo não encontrado.')
        pressione_enter()

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
