import psycopg2
from src.utils import *
from tabulate  import tabulate
from src.logs  import GerenciadorLogs

class Database:
    def __init__(self, host, database, user, password, port):
        self.host       = host
        self.database   = database
        self.user       = user
        self.password   = password
        self.port       = port
        self.connection = None
        self.cursor     = None
        self.logger     = GerenciadorLogs().obter_logger()

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

        except Exception as e:
            self.logger.error(f"Erro ao conectar: {e}")
            raise

    def desconectar(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            self.logger.info("Conexão fechada com sucesso.")
        else:
            self.logger.warning("Nenhuma conexão ativa para fechar.")

    def iniciar_transacao(self):
        if self.connection:
            self.connection.autocommit = False
            self.logger.info("Transação iniciada.")
        else:
            self.logger.error("Conexão não estabelecida para iniciar transação.")

    def commit(self):
        if self.connection:
            self.connection.commit()
            self.connection.autocommit = True
            self.logger.info("Commit.")

    def rollback(self):
        if self.connection:
            self.connection.rollback()
            self.connection.autocommit = True
            self.logger.info("Rollback.")

    def executar_script(self, script, values = None):
        if not self.cursor:
            self.logger.error("Erro: Conexão não estabelecida ou cursor não disponível.")
            return
        try:
            self.cursor.execute(script, values)
            self.commit()
            return True

        except Exception as e:
            self.logger.error(f"Erro ao executar o script: {e}")
            self.rollback()
            return False

    def criar_tabela(self, nome_tabela: str, campos: dict[str, str]) -> None:
        campos_str = ', '.join(
            [f'{campo} {tipo}' for campo, tipo in campos.items()]
        )
        script = f"""
            CREATE TABLE IF NOT EXISTS {nome_tabela} (
                {campos_str}
            );
        """
        if self.executar_script(script):
            self.logger.info(f'Criando tabela {nome_tabela}')

    def insert(self, tabela: str, campos_valores: dict) -> bool:
        colunas = list(campos_valores.keys())
        valores = list(campos_valores.values())

        campos       = ', '.join(colunas)
        placeholders = ', '.join(['%s'] * len(colunas))

        script = f"""
            INSERT INTO {tabela} (
                {campos}
            )
            VALUES (
                {placeholders}
            );
        """
        self.iniciar_transacao()
        self.logger.info(f'Realizando Insert na tabela {tabela}')

        if self.executar_script(script, valores):
            self.logger.info(f'Insert realizado com sucesso.')
            self.commit()
            return True
        else:
            self.logger.error(f'Insert falhou.')
            self.rollback()
            return False

    def update(self, tabela: str, campos_valores: dict, condicao: dict) -> bool:
        colunas  = list(campos_valores.keys())
        valores  = list(campos_valores.values())
        set_expr = ', '.join([f'{coluna} = %s' for coluna in colunas])

        condicoes     = [f'{campo} = %s' for campo in condicao.keys()]
        condicao_expr = ' AND '.join(condicoes)

        script = f"""
            UPDATE {tabela}
               SET {set_expr}
             WHERE {condicao_expr};
        """

        self.iniciar_transacao()
        self.logger.info(f'Realizando Update na tabela {tabela}')

        valores_completos = valores + list(condicao.values())

        if self.executar_script(script, valores_completos):
            self.logger.info(f'Update realizado com sucesso.')
            self.commit()
            return True
        else:
            self.logger.error(f'Update falhou.')
            self.rollback()
            return False

    def adicionar_coluna(self, tabela, nome_campo, tipo_campo):
        script = f"ALTER TABLE {tabela} ADD COLUMN {nome_campo} {tipo_campo};"

        self.iniciar_transacao()
        self.logger.info(f"Adicionando coluna {nome_campo} na tabela {tabela}.")

        if self.executar_script(script):
            self.commit()
        else:
            self.rollback()

    def remover_coluna(self, tabela, nome_coluna):
        script = f"ALTER TABLE {tabela} DROP COLUMN {nome_coluna};"

        self.iniciar_transacao()
        self.logger.info(f"Removendo coluna {nome_coluna} da tabela {tabela}.")

        if self.executar_script(script):
            self.logger.info('A Coluna foi removida.')
            self.commit()
        else:
            self.logger.error('A Coluna não foi removida.')
            self.rollback()

    def exibir_tabela(self, registros, titulos: list[str], indices: list[int], titulo_tabela: str = ''):
        if registros:
            tabela = [[registro[i] for i in indices] for registro in registros]

            if titulo_tabela:
                titulo(titulo_tabela)

            print(tabulate(
                tabela,
                headers=titulos,
                tablefmt="grid",
                colalign=["center"] * len(titulos)
            ))
        else:
            print('Nenhum registro encontrado.')

    def listar_registros(self, nome_tabela: str, colunas: list, indices: list, campo_order_by: str = None):
        try:
            self.executar_script(f'SELECT * FROM {nome_tabela} ORDER BY {campo_order_by}')
            registros = self.cursor.fetchall()

            if registros:
                tabela = [
                    [registro[i] for i in indices] for registro in registros
                ]
                print(tabulate(
                    tabela,
                    headers=colunas,
                    tablefmt="grid",
                    colalign=["center"] * len(colunas)
                ))
            else:
                print(f'Nenhum registro encontrado para {nome_tabela}.')

        except Exception as e:
            print(f'Erro ao listar registros de {nome_tabela}: {e}')

    def buscar(self, nome_tabela: str, campo_id: str, id: int):
        try:
            self.executar_script(f"SELECT * FROM {nome_tabela} WHERE {campo_id} = %s", (id,))
            resultado = self.cursor.fetchall()

            if resultado:
                return resultado[0]
            return None

        except Exception as e:
            self.logger.error(f'Erro ao buscar registros na tabela {nome_tabela}: {e}')
            self.rollback()
            return None

    def excluir_por_id(self, nome_tabela: str, campo_id: str, valor_id: int):
        self.iniciar_transacao()
        self.logger.info(f'Iniciando exclusão na tabela {nome_tabela}.')
        try:
            if self.executar_script(f'DELETE FROM {nome_tabela} WHERE {campo_id} = %s', (valor_id,)):
                print_log_error(f'Registro excluido na tabela {nome_tabela}.')
                self.commit()
                return True
            else:
                print_log_error(f'Erro ao excluir registro na tabela {nome_tabela}.')
                self.rollback()
                return False

        except Exception as e:
            self.logger.error(f'Erro ao excluir registro na tabela {nome_tabela}. {e}')
            self.rollback()
            return False
