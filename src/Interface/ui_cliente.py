from src.utils  import *
from .ui        import Ui
from src.models import Clientes
from src.instances.db_instance import db

class TelaCliente(Ui):
    def __init__(self):
        pass

    def cadastrar_cliente(self):
        titulo('Insira as informações do cliente')

        respostas = [
            perguntar('Nome'),
            perguntar('CPF'),
            perguntar('Email'),
            perguntar('Telefone'),
            perguntar('Data de Nascimento [AAAA-MM-DD]'),
            perguntar('CEP'),
            selecionar('Status do Cliente', ['ATIVO', 'INATIVO'])
        ]

        dados = {
            "nome"            : respostas[0],
            "cpf"             : respostas[1],
            "email"           : respostas[2],
            "telefone"        : respostas[3],
            "data_nascimento" : respostas[4],
            "cep"             : respostas[5],
            "status"          : respostas[6],
        }

        cliente = Clientes(
            dados["nome"],
            dados["cpf"],
            dados["email"],
            dados["telefone"],
            dados["data_nascimento"],
            dados["cep"],
            dados["status"]
        )
        cliente.cadastrar()
        pressione_enter()

    def listar_clientes(self):
        colunas_cliente = ['CÓDIGO', 'NOME', 'CPF', 'E-MAIL', 'TELEFONE', 'DATA DE NASCIMENTO', 'CEP', 'STATUS']
        indices_cliente = [0, 1, 2, 3, 4, 5, 6, 7]

        db.listar_registros('CLIENTES', colunas_cliente, indices_cliente, 'CLI_CODIGO')
        pressione_enter()

    def editar_cliente(self):
        codigo_cliente     = perguntar('Digite o código do cliente que deseja alterar')
        cliente_encontrado = db.buscar('CLIENTES', 'CLI_CODIGO', codigo_cliente)

        titulo(f'Cliente encontrado: {cliente_encontrado[1]}'.upper())

        respostas = [
            perguntar(f'Nome atual: {cliente_encontrado[1]}\n  Novo nome:'),
            perguntar(f'CPF atual: {cliente_encontrado[2]}\n  Novo CPF:'),
            perguntar(f'E-mail atual: {cliente_encontrado[3]}\n  Novo E-mail:'),
            perguntar(f'Telefone atual: {cliente_encontrado[4]}\n  Novo Telefone:'),
            perguntar(f'Data de Nascimento atual: {cliente_encontrado[5]}\n  Nova Data de Nascimento [AAAA-MM-DD]:'),
            perguntar(f'CEP atual: {cliente_encontrado[6]}\n  Novo CEP:'),
            selecionar(f'Status atual: {cliente_encontrado[7]}\n  Novo Status (ATIVO ou INATIVO):', ['ATIVO', 'INATIVO'])
        ]

        dados = {
            "nome"            : respostas[0] or cliente_encontrado[1],
            "cpf"             : respostas[1] or cliente_encontrado[2],
            "email"           : respostas[2] or cliente_encontrado[3],
            "telefone"        : respostas[3] or cliente_encontrado[4],
            "data_nascimento" : respostas[4] or cliente_encontrado[5],
            "cep"             : respostas[5] or cliente_encontrado[6],
            "status"          : respostas[6] or cliente_encontrado[7]
        }

        cliente = Clientes(
            dados["nome"],
            dados["cpf"],
            dados["email"],
            dados["telefone"],
            dados["data_nascimento"],
            dados["cep"],
            dados["status"]
        )
        cliente.editar(codigo_cliente)
        pressione_enter()

    def excluir_cliente(self):
        codigo_cliente     = perguntar('Digite o código do cliente que deseja excluir')
        cliente_encontrado = db.buscar('CLIENTES', 'CLI_CODIGO', codigo_cliente)

        if cliente_encontrado:
            titulo(f'Cliente encontrado: {cliente_encontrado[1]}'.upper())
            resposta = perguntar('Tem certeza que deseja excluir? [S/N]').strip().lower()

            if resposta and resposta[0] == 's':
                db.excluir_por_id('CLIENTES', 'CLI_CODIGO', codigo_cliente)
            else:
                print('\nExclusão cancelada.')
        else:
            print('\nCliente não encontrado.')
        pressione_enter()

    def exibir(self):
        limpar_terminal()

        titulo('Tela de Clientes')
        opcao = montar_opcoes(
            "1. Cadastrar Cliente",
            "2. Listar Clientes",
            "3. Editar Cliente",
            "4. Excluir Cliente",
            "5. Voltar ao Menu Principal"
        )

        limpar_terminal()

        match opcao:
            case 1:
                self.cadastrar_cliente()
            case 2:
                self.listar_clientes()
            case 3:
                self.editar_cliente()
            case 4:
                self.excluir_cliente()
            case 5:
                print("Voltando ao Menu Principal...")
                return
