from ..Utils import *
from ..Enum  import Status
from ..Logs  import GerenciadorLogs
from ..Instances.db_instance import db

class Clientes():
    def __init__(self, nome, cpf, email, telefone, data_nascimento, cep, status: Status):
        self.nome            = nome
        self.cpf             = cpf
        self.email           = email
        self.telefone        = telefone
        self.data_nascimento = data_nascimento
        self.cep             = cep
        self.status          = status
        self.logger          = GerenciadorLogs().obter_logger()
        
    def cadastrar(self):     
        db.iniciar_transacao()
        try:
            script = """
                INSERT INTO CLIENTES (
                    CLI_NOME,
                    CLI_CPF, 
                    CLI_EMAIL,
                    CLI_TELEFONE, 
                    CLI_DATA_NASCIMENTO,
                    CLI_CEP, 
                    CLI_STATUS
                ) 
                VALUES (
                    %s, 
                    %s, 
                    %s, 
                    %s, 
                    %s, 
                    %s, 
                    %s
                );
            """
            values = (self.nome, self.cpf, self.email, self.telefone, self.data_nascimento, self.cep, self.status)

            if db.executar_script(script, values):
                print('Cliente cadastrado com sucesso!') 
            else:
                print('Erro ao cadastrar cliente!')
                self.logger.error(f'Erro ao cadastrar cliente.')
                db.rollback()

        except Exception as e:
            db.rollback()
            self.logger.error(f'Erro ao cadastrar cliente. {e}')
        
    @staticmethod
    def listar():
        titulo('Listando Clientes')
        
        script = 'SELECT * FROM CLIENTES'
        db.executar_script(script)
        clientes = db.cursor.fetchall()

        if clientes:
            for cliente in clientes:
                print(f'Código: {cliente[0]}, Nome: {cliente[1]}, CPF: {cliente[2]}, Status: {cliente[7]}')
        else:
            print('Nenhum cliente encontrado.')