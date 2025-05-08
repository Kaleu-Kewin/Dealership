import psycopg2
from src.Logs.logger import GerenciadorLogs

class Database:
    def __init__(self, host, database, user, password, port):
        self.host       = host
        self.database   = database
        self.user       = user
        self.password   = password
        self.port       = port
        self.connection = None
        self.cursor     = None
        
        gerenciador_logs = GerenciadorLogs()
        self.logger      = gerenciador_logs.obter_logger()

    def conectar(self):
        self.logger.info(f"Iniciando o script de conexão ao banco de dados.")
        try:
            self.connection = psycopg2.connect(
                host     = self.host,
                database = self.database,
                user     = self.user,
                password = self.password,
                port     = self.port
            )
            self.cursor = self.connection.cursor()  
            self.logger.info("Conexão estabelecida com sucesso.")
            return self.connection
        
        except Exception as erro:
            self.logger.error(f"Erro ao conectar: {erro}")
            raise

    def desconectar(self):
        if self.connection:
            self.cursor.close()  
            self.connection.close() 
            self.logger.info("Conexão fechada com sucesso.")
        else:
            self.logger.warning("Nenhuma conexão ativa para fechar.")
    
    def executar_script(self, script):
        if not self.cursor:
            self.logger.error("Erro: Conexão não estabelecida ou cursor não disponível.")
            return
        try:
            self.cursor.execute(script)
            self.connection.commit()
        except Exception as e:
            self.logger.error(f"Erro ao executar o script: {e}")
            self.connection.rollback()

    def criar_tabela(self, nome_tabela, campos):
        campos_str = ", ".join(
            [f"{campo} {tipo}" for campo, tipo in campos.items()]
        )
        self.logger.info(f"Criando tabela {nome_tabela}...")
        script = f"CREATE TABLE IF NOT EXISTS {nome_tabela} ({campos_str});"
        self.executar_script(script)
    
    def adicionar_coluna(self, tabela, nome_campo, tipo_campo):
        script = f"ALTER TABLE {tabela} ADD COLUMN {nome_campo} {tipo_campo};"
        self.executar_script(script)

    def remover_coluna(self, tabela, nome_coluna):
        script = f"ALTER TABLE {tabela} DROP COLUMN {nome_coluna};"
        self.executar_script(script)
