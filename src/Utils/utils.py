import os

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