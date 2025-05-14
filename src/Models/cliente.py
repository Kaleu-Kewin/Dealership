from ..utils import *
from ..Enum  import Status
from ..logs  import GerenciadorLogs
from ..instances.db_instance import db

class Clientes():
    logger = GerenciadorLogs().obter_logger()

    def __init__(self, nome, cpf, email, telefone, data_nascimento, cep, status: Status):
        self.nome            = nome
        self.cpf             = cpf
        self.email           = email
        self.telefone        = telefone
        self.data_nascimento = data_nascimento
        self.cep             = cep
        self.status          = status

    def cadastrar(self):
        db.iniciar_transacao()
        self.logger.info(f'Iniciando cadastro de cliente.')
        try:
            if db.insert(
                "CLIENTES",
                {
                    "CLI_NOME"            : self.nome,
                    "CLI_CPF"             : self.cpf,
                    "CLI_EMAIL"           : self.email,
                    "CLI_TELEFONE"        : self.telefone,
                    "CLI_DATA_NASCIMENTO" : self.data_nascimento,
                    "CLI_CEP"             : self.cep,
                    "CLI_STATUS"          : self.status
                }
            ):
                print_log_info('Cliente cadastrado com sucesso!')
            else:
                print_log_error('Erro ao cadastrar cliente.')

        except Exception as e:
            db.rollback()
            self.logger.error(f'Erro ao cadastrar cliente. {e}')

    def editar(self, codigo_cliente: int):
        db.iniciar_transacao()
        self.logger.info(f'Iniciando atualização de cliente.')
        try:
            if db.update(
                "CLIENTES",
                {
                    "CLI_NOME"            : self.nome,
                    "CLI_CPF"             : self.cpf,
                    "CLI_EMAIL"           : self.email,
                    "CLI_TELEFONE"        : self.telefone,
                    "CLI_DATA_NASCIMENTO" : self.data_nascimento,
                    "CLI_CEP"             : self.cep,
                    "CLI_STATUS"          : self.status
                },
                {
                    "CLI_CODIGO"          : codigo_cliente
                }
            ):
                print_log_info('Cliente editado com sucesso!')
            else:
                print_log_error('Erro ao editar informações do cliente.')

        except Exception as e:
            db.rollback()
            self.logger.error(f'Erro ao atualizar cliente. {e}')

    @staticmethod
    def excluir(codigo_cliente: int):
        db.excluir_por_id('CLIENTES', 'CLI_CODIGO', codigo_cliente)

    @staticmethod
    def listar():
        colunas_cliente = ['CÓDIGO', 'NOME', 'CPF', 'E-MAIL', 'TELEFONE', 'DATA DE NASCIMENTO', 'CEP', 'STATUS']
        indices_cliente = [0, 1, 2, 3, 4, 5, 6, 7]

        db.listar_registros('CLIENTES', colunas_cliente, indices_cliente, 'CLI_CODIGO')

    @staticmethod
    def buscar(codigo_cliente: int):
        return db.buscar('CLIENTES', 'CLI_CODIGO', codigo_cliente)
