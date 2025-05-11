from ..Utils    import *
from .ui        import Ui
from ..Models   import Clientes
from ..Enum     import Status as s

class TelaCliente(Ui): 
    def __init__(self):
        pass
    
    def cadastrar_cliente(self):
        titulo('Insira as informações do cliente')

        perguntas = [
            perguntar('Nome'),
            perguntar('CPF'),
            perguntar('Email'),
            perguntar('Telefone'),
            perguntar('Data de Nascimento [AAAA-MM-DD]'),
            perguntar('CEP'),
            selecionar('Status do Cliente', ['ATIVO', 'INATIVO'])
        ]

        dados = {
            "nome"            : perguntas[0],
            "cpf"             : perguntas[1],
            "email"           : perguntas[2],
            "telefone"        : perguntas[3],
            "data_nascimento" : perguntas[4],
            "cep"             : perguntas[5],
            "status"          : perguntas[6],
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
        Clientes.listar() 
        pressione_enter()
        
    def editar_cliente(self):
        codigo_cliente     = perguntar('Digite o código do cliente que deseja alterar')
        cliente_encontrado = Clientes.buscar(codigo_cliente)

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