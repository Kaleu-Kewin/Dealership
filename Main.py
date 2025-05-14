from src.interface import Login
from src.utils     import tratar_erros
from src.scripts   import criar_tabelas

@tratar_erros
def main():
    criar_tabelas()

    login = Login()
    login.exibir()

if __name__ == "__main__":
    main()
