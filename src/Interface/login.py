from src.instances.db_instance import db
from src.utils import *
from .menu import Menu
from .ui import Ui
import hashlib

class Login(Ui):
    def __init__(self):
        self.menu = Menu()

    def validar_login(self, nome: str, senha: str) -> bool:
        try:
            script = """
                SELECT USU_SENHA
                  FROM USUARIOS
                 WHERE USU_NOME = %s
            """
            db.executar_script(script, (nome,))
            resultado = db.cursor.fetchone()

            if resultado:
                senha_salva = resultado[0]
                senha_hash  = hashlib.sha256(senha.encode()).hexdigest()
                return senha_hash == senha_salva
            return False

        except Exception as e:
            db.logger.error(f"Erro ao validar login: {e}")
            return False

    def logar(self):
        while True:
            limpar_terminal()

            titulo('Preencha as informações para o login')

            respostas = [
                perguntar('Digite seu usuário'),
                perguntar_senha('Digite sua senha'),
            ]

            nome  = respostas[0].upper()
            senha = respostas[1]

            if not self.validar_login(nome, senha):
                print('\nLogin inválido! Tente novamente.')
                pressione_enter()
            else:
                print('\nLogin realizado com sucesso!')
                pressione_enter()
                self.menu.exibir()

    def exibir(self):
        titulo('Seja bem vindo!')

        opcao = montar_opcoes(
            '1. Realizar Login.',
            '2. Sair.'
        )

        match opcao:
            case 1:
                self.logar()
            case 2:
                print('Finalizando programa...')
                exit()
