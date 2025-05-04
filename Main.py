from decimal import Decimal
from src     import Carro, Clientes, Contato, Concessionaria, Cores as c

def main():
    concessionaria = Concessionaria('Super carros')

    honda_civic = Carro(
        'Honda Civic', 
        'Honda', 
        '2020', 
        c.Preto, 
        '89000.00'
    )
    
    fiat_uno = Carro(
        'Fiat Uno', 
        'Fiat', 
        '2012', 
        c.Prata, 
        '18000.00'
    )

    contato = Contato(['cliente@gmail.com', '(14) 99123-4567'])
    cliente = Clientes('Kaléu', 19, contato, Decimal('120000.00'))

    cliente.contatos_vinculados()

    concessionaria.adicionar_veiculo(honda_civic)
    concessionaria.adicionar_veiculo(honda_civic)
    concessionaria.adicionar_veiculo(fiat_uno)

    concessionaria.veiculos_em_estoque()

    concessionaria.vender_veiculo(honda_civic, cliente)
    concessionaria.vender_veiculo(honda_civic, cliente)
    concessionaria.vender_veiculo(fiat_uno, cliente)

    cliente.veiculos_vinculados()

if __name__ == "__main__":
    main()