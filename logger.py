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
    
    def get_logger(self):
        raise NotImplementedError
    
class MainLogger(Loggers):
    def __init__(self):
        super().__init__()
        self.set_formatter()
        self.set_handlers()

    def get_logger(self, name: str):
        # cria meu logger e define o nível
        logger = logging.getLogger('main')
        logger.setLevel(logging.INFO)

        if not logger.hasHandlers():
            logger.addHandler(self.file_handler)
            logger.addHandler(self.stream_handler)

        return logger

    def set_formatter(self):
        self.main_formatter = logging.Formatter(fmt=self.format1)

    def set_handlers(self): 
        # utiliza o formato nos handlers    
        self.file_handler.setFormatter(self.main_formatter)
        self.stream_handler.setFormatter(self.main_formatter)

class ScrapLogger(Loggers):
    def __init__(self):
        super().__init__()
        self.set_formatter()
        self.set_handlers()

    def get_logger(self, name: str):
        logger = logging.getLogger('scrapers')
        logger.setLevel(logging.DEBUG)

        if not logger.hasHandlers():
            logger.addHandler(self.file_handler)
            logger.addHandler(self.stream_handler)

        return logger
    
    def set_formatter(self):
        self.main_formatter = logging.Formatter(fmt=self.format1)

    def set_handlers(self): 
        # utiliza o formato nos handlers    
        self.file_handler.setFormatter(self.main_formatter)
        self.stream_handler.setFormatter(self.main_formatter)