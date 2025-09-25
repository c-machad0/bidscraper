import logging
import sys

def main_logger(name: str):
    format1 = "%(levelname)s|%(name)s|%(asctime)s|%(message)s|%(filename)s|%(lineno)d"

    stream_handler = logging.StreamHandler(sys.stdout) # informa a saída para o console

    file_handler = logging.FileHandler( # cria meu próprio handler
        filename='log.log',
        mode='w',
        encoding='utf-8',
    )

    main_formatter = logging.Formatter(fmt=format1) # formata os handlers criados

    # utiliza o formato nos handlers
    file_handler.setFormatter(main_formatter)
    stream_handler.setFormatter(main_formatter)

    # configura o root logger
    logging.basicConfig(handlers=[file_handler, stream_handler])
    
    # cria meu logger e define o nível
    logger = logging.getLogger('main')
    logger.setLevel(logging.INFO)

    return logger