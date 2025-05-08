import os
import logging
from logging import FileHandler, Formatter, Filter, getLogger

CAMINHO_LOGS = "src/Logs"
os.makedirs(CAMINHO_LOGS, exist_ok=True)

FORMATO_LOG = Formatter('%(asctime)s - %(levelname)s - %(message)s')

class FiltroExecucao(Filter):
    def filter(self, record):
        return record.levelno < logging.ERROR

class FiltroErro(Filter):
    def filter(self, record):
        return record.levelno >= logging.ERROR

def criar_handler(caminho: str, nivel: int, filtro: Filter) -> FileHandler:
    handler = FileHandler(caminho, encoding='utf-8')
    handler.setLevel(nivel)
    handler.setFormatter(FORMATO_LOG)
    handler.addFilter(filtro)
    return handler

handler_execucao = criar_handler(f"{CAMINHO_LOGS}/execution.log", logging.INFO, FiltroExecucao())
handler_erro     = criar_handler(f"{CAMINHO_LOGS}/errors.log", logging.ERROR, FiltroErro())

logger = getLogger('concessionaria_logger')
logger.setLevel(logging.DEBUG)

if not logger.hasHandlers():
    logger.addHandler(handler_execucao)
    logger.addHandler(handler_erro)