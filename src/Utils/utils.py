import os
from InquirerPy import inquirer

def limpar_terminal() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        
def montar_opcoes(*args) -> int:
    while True:
        for opcao in args:
            print(opcao)
        try:
            escolha = int(input("\nEscolha uma opção: "))
            if 0 <= escolha <= len(args):
                return escolha
            else:
                print("Opção inválida. Tente novamente.\n")
        except ValueError:
            print("Digite um número válido.\n")
            
def titulo(titulo: str) -> None:
    print(f'\n--- {titulo} ---\n')
    
def perguntar(texto: str) -> str:
    return inquirer.text(message=texto).execute()

def selecionar(texto: str, opcoes: list[str]) -> str:
    return inquirer.select(message=texto, choices=opcoes).execute()
