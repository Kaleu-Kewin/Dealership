from ..Utils  import *
from ..Enum   import Status
from tabulate import tabulate
from ..Logs   import GerenciadorLogs
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
        self.logger.info(f'Iniciando cadastro de cliente.')
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
                    self.logger.info(f'O Cliente foi cadastrado com sucesso.')
            else:
                print('Erro ao cadastrar cliente!')
                self.logger.error(f'Erro ao cadastrar cliente.')
                db.rollback()
                
        except Exception as e:
            db.rollback()
            self.logger.error(f'Erro ao cadastrar cliente. {e}')
            
    def editar(self, codigo_cliente):
        db.iniciar_transacao()
        self.logger.info(f'Iniciando atualização de cliente.')
        try:
            script = """
                UPDATE CLIENTES
                SET 
                    CLI_NOME            = %s,
                    CLI_CPF             = %s, 
                    CLI_EMAIL           = %s,
                    CLI_TELEFONE        = %s, 
                    CLI_DATA_NASCIMENTO = %s,
                    CLI_CEP             = %s, 
                    CLI_STATUS          = %s
                WHERE CLI_CODIGO        = %s;
            """
            sets = (self.nome, self.cpf, self.email, self.telefone, self.data_nascimento, self.cep, self.status, codigo_cliente)

            if db.executar_script(script, sets):
                print('Cliente atualizado com sucesso!') 
                self.logger.info(f'O Cliente foi atualizado com sucesso.')
            else:
                print('Erro ao atualizar cliente!')
                self.logger.error(f'Erro ao atualizar cliente.')
                db.rollback() 
                    
        except Exception as e:
            db.rollback()
            self.logger.error(f'Erro ao atualizar cliente. {e}')
       
    @staticmethod     
    def exibir(clientes):
        if clientes:
            tabela = [
                [cliente[0], cliente[1], cliente[2], cliente[3], cliente[4], cliente[7]]
                for cliente in clientes
            ]
            titulo('Listando Cliente(s)')
            print(tabulate(
                tabela, 
                headers=[
                    'Código',
                    'Nome', 
                    'CPF',
                    'E-mail', 
                    'Telefone', 
                    'Status'], 
                tablefmt="grid",
                colalign=['center'] * 6))
        else:
            print('Nenhum cliente encontrado.')        
        
    @staticmethod
    def listar():
        db.executar_script('SELECT * FROM CLIENTES ORDER BY CLI_CODIGO')
        clientes = db.cursor.fetchall()
        Clientes.exibir(clientes)
          
    @staticmethod
    def buscar(codigo_cliente: int):
        db.executar_script(f'SELECT * FROM CLIENTES WHERE CLI_CODIGO = {codigo_cliente}')
        clientes = db.cursor.fetchall()
        if clientes:
            return clientes[0]  
        return None