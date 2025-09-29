import logging
import sys

class Loggers:
    def __init__(self):
        self.format1 = "%(levelname)s|%(name)s|%(asctime)s|%(message)s|%(filename)s|%(lineno)d"
        self.file_handler = logging.FileHandler( # cria meu próprio handler
            filename='bidscraper.log',
            mode='a',
            encoding='utf8'
        )
        self.stream_handler = logging.StreamHandler(sys.stdout) # informa a saída para o console
        self.set_formatter()
        self.set_handlers()

    def get_logger(self, name: str):
         # cria meu logger e define o nível
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        if not logger.hasHandlers():
            logger.addHandler(self.file_handler)
            logger.addHandler(self.stream_handler)

        return logger
 
    def set_formatter(self):
        self.bid_formatter = logging.Formatter(fmt=self.format1)

    def set_handlers(self): 
        # utiliza o formato nos handlers    
        self.file_handler.setFormatter(self.bid_formatter)
        self.stream_handler.setFormatter(self.bid_formatter)
