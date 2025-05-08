import psycopg2
from src.Logs.logger import logger 

class Database:
    def __init__(self, host, database, user, password, port):
        self.host       = host
        self.database   = database
        self.user       = user
        self.password   = password
        self.port       = port
        self.connection = None
        self.cursor     = None

    def conectar(self):
        logger.info(f"Iniciando o script de conexão ao banco de dados.")
        logger.info(f"Tentando conectar ao banco de dados {self.database} em {self.host}:{self.port}...")
        try:
            self.connection = psycopg2.connect(
                host     = self.host,
                database = self.database,
                user     = self.user,
                password = self.password,
                port     = self.port
            )
            self.cursor = self.connection.cursor()  
            logger.info("Conexão estabelecida com sucesso.")
            return self.connection
        
        except Exception as erro:
            logger.error(f"Erro ao conectar: {erro}")
            raise

    def desconectar(self):
        if self.connection:
            self.cursor.close()  
            self.connection.close() 
            logger.info("Conexão fechada com sucesso.")
        else:
            logger.warning("Nenhuma conexão ativa para fechar.")
    
    def executar_script(self, script):
        if not self.cursor:
            logger.error("Erro: Conexão não estabelecida ou cursor não disponível.")
            return
        try:
            self.cursor.execute(script)
            self.connection.commit()
            logger.info("Script executado com sucesso.")
        except Exception as e:
            logger.error(f"Erro ao executar o script: {e}")
            self.connection.rollback()
    
    def adicionar_coluna(self, tabela, nome_campo, tipo_campo):
        script = f"ALTER TABLE {tabela} ADD COLUMN {nome_campo} {tipo_campo};"
        self.executar_script(script)

    def remover_coluna(self, tabela, nome_coluna):
        script = f"ALTER TABLE {tabela} DROP COLUMN {nome_coluna};"
        self.executar_script(script)
