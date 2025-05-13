from src.Interface import Login
from src.Utils     import tratar_erros
from src.Scripts   import criar_tabelas

@tratar_erros
def main():
    criar_tabelas()
    login = Login()
    login.exibir()

if __name__ == "__main__":
    main()
