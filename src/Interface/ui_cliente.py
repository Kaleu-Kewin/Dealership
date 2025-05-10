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
        
    def listar_clientes(self):
        Clientes.listar()  
        
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