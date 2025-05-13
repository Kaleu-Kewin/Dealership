import os
from decimal    import Decimal
from InquirerPy import inquirer
from src.Logs   import GerenciadorLogs

log = GerenciadorLogs()

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

def perguntar_senha(texto: str) -> str:
        return inquirer.secret(message=texto).execute()

def selecionar(texto: str, opcoes: list[str]) -> str:
    return inquirer.select(message=texto, choices=opcoes).execute()

def pressione_enter():
    input('\nPressione Enter para continuar...')
    limpar_terminal()

def validar_preco(preco):
    if isinstance(preco, str):
        preco = preco.replace('R$', '').replace(' ', '').replace(',', '.')
    try:
        return Decimal(preco)
    except:
        log.logger.error(f'Valor de preço inválido: {preco}')

def print_log_info(mensagem):
    print(f'\n{mensagem}')
    log.logger.info(mensagem)

def print_log_error(mensagem):
    print(f'\n{mensagem}')
    log.logger.error(mensagem)

def tratar_erros(funcao):
    def wrapper(*args, **kwargs):
        try:
            return funcao(*args, **kwargs)

        except KeyboardInterrupt:
            print("\nFinalizando programa...")
            exit()

        except Exception as e:
            print(f"\nOcorreu um erro: {e}")

    return wrapper
