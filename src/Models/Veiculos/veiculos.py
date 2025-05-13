from src.Instances.db_instance import db
from src.Enum  import Cores, TipoVeiculo
from src.Logs  import GerenciadorLogs
from decimal   import Decimal
from abc       import ABC
from src.Utils import *

class Veiculos(ABC):
    def __init__(self, modelo: str, marca: str, ano: int, preco: Decimal, cor: Cores, quantidade: int, placa: str, tipo_veiculo: TipoVeiculo):
        self.modelo       = modelo
        self.marca        = marca
        self.ano          = ano
        self.preco        = Decimal(preco)
        self.cor          = cor
        self.quantidade   = quantidade
        self.placa        = placa
        self.tipo_veiculo = tipo_veiculo

class VeiculosDAO:
    def __init__(self, veiculo: Veiculos):
        self.logger  = GerenciadorLogs().obter_logger()
        self.veiculo = veiculo

    def cadastrar_veiculo(self):
        db.iniciar_transacao()
        self.logger.info(f'Iniciando cadastro de veiculo.')
        try:
            if db.insert(
                "VEICULOS",
                {
                    "VEI_MODELO"     : self.veiculo.modelo,
                    "VEI_MARCA"      : self.veiculo.marca,
                    "VEI_ANO"        : self.veiculo.ano,
                    "VEI_PRECO"      : self.veiculo.preco,
                    "VEI_COR"        : self.veiculo.cor,
                    "VEI_QUANTIDADE" : self.veiculo.quantidade,
                    "VEI_PLACA"      : self.veiculo.placa,
                    "TIPO_VEICULO"   : self.veiculo.tipo_veiculo
                }
            ):
                print_log_info('Veiculo cadastrado com sucesso.')
            else:
                print_log_error('Erro ao cadastrar Veiculo.')

        except Exception as e:
            db.rollback()
            self.logger.error(f'Erro ao cadastrar Veiculo. {e}')
