import os
import logging
from logging import FileHandler, Formatter, Filter, getLogger

class GerenciadorLogs:
    CAMINHO_LOGS = "src/Logs"
    FORMATO_LOG  = Formatter('%(asctime)s - %(levelname)s - %(message)s')

    class FiltroErro(Filter):
        def filter(self, record):
            return record.levelno >= logging.WARNING

    def __init__(self, nome_logger: str = 'concessionaria_logger'):
        self.logger = getLogger(nome_logger)
        self._criar_diretorio_logs()
        self._configurar_logger()

    def _criar_diretorio_logs(self):
        os.makedirs(self.CAMINHO_LOGS, exist_ok=True)

    def _criar_handler(self, caminho: str, nivel: int, filtro: Filter = None) -> FileHandler:
        handler = FileHandler(caminho, encoding='utf-8')
        handler.setLevel(nivel)
        handler.setFormatter(self.FORMATO_LOG)
        
        if filtro:
            handler.addFilter(filtro)
        return handler

    def _configurar_logger(self):
        self.logger.setLevel(logging.DEBUG)

        if not self.logger.hasHandlers():
            handler_execucao = self._criar_handler(f"{self.CAMINHO_LOGS}/execution.log", logging.DEBUG)
            handler_erro     = self._criar_handler(f"{self.CAMINHO_LOGS}/errors.log", logging.ERROR, self.FiltroErro())

            self.logger.addHandler(handler_execucao)
            self.logger.addHandler(handler_erro)

    def obter_logger(self):
        return self.logger
    
def log(self, nivel: int, mensagem: str):
    logs = {
        logging.DEBUG    : self.logger.debug,
        logging.INFO     : self.logger.info,
        logging.WARNING  : self.logger.warning,
        logging.ERROR    : self.logger.error,
        logging.CRITICAL : self.logger.critical
    }
    try:
        logs[nivel](mensagem)
    except KeyError:
        raise ValueError("Nível de log inválido.")

gerenciador_logs = GerenciadorLogs()
logger = gerenciador_logs.obter_logger()
