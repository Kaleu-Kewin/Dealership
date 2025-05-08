from src.Interface import Menu
from src.Scripts   import criar_tabelas

def main(): 
    criar_tabelas()
    menu = Menu()
    menu.exibir()

if __name__ == "__main__":
    main()