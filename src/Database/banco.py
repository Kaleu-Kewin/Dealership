import psycopg2
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
        logging.info(f"Iniciando o script de conexão ao banco de dados.")
        logging.info(f"Tentando conectar ao banco de dados {self.database} em {self.host}:{self.port}...")
        logging.info(f"Usuário: {self.user}")
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            self.cursor = self.connection.cursor()  
            logging.info("Conexão estabelecida com sucesso.")
            return self.connection
        
        except Exception as erro:
            logging.error(f"Erro ao conectar: {erro}")
            raise

    def desconectar(self):
        if self.connection:
            self.cursor.close()  
            self.connection.close() 
            logging.info("Conexão e cursor fechados com sucesso.")
        else:
            logging.warning("Nenhuma conexão ativa para fechar.")
    
    def executar_script(self, script):
        if not self.cursor:
            logging.error("Erro: Conexão não estabelecida ou cursor não disponível.")
            return
        try:
            self.cursor.execute(script)
            self.connection.commit()
            logging.info("Script executado com sucesso.")
        except Exception as e:
            logging.error(f"Erro ao executar o script: {e}")
            self.connection.rollback()
    
    def adicionar_coluna(self, tabela, nome_campo, tipo_campo):
        script = f"ALTER TABLE {tabela} ADD COLUMN {nome_campo} {tipo_campo};"
        self.executar_script(script)

    def remover_coluna(self, tabela, nome_coluna):
        script = f"ALTER TABLE {tabela} DROP COLUMN {nome_coluna};"
        self.executar_script(script)