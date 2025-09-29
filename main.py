"""
main.py

Ponto de entrada para execução do scraping de licitações municipais.
Orquestra execução dos scrapers específicos por município e atualização do banco de dados.
"""

from database import BidDatabase
from scrapers import (BidScraperItajuipe, BidScraperItapitanga, 
                      BidScraperAlmadina, BidScraperIbicarai, BidScraperUbaitaba, 
                      BidScraperBarroPreto, BidScraperItape)
from logger import Loggers

logger_main = Loggers().get_logger('main')

def run_database():
    """
    Cria conexão com o banco, cria tabela se necessário, atualiza dados a partir de arquivos JSON
    e encerra conexão.
    """
    db = BidDatabase()
    db.create_table()
    db.update_table()
    db.close_database()

if __name__ == '__main__':
    """
    Executa os scrapers para todos os municípios definidos.
    Depois de cada scrape, atualiza o banco de dados com os novos dados.
    """
    logger_main.info('Scraper sendo iniciado')
    try:
        scrapers = [
            BidScraperItajuipe(),
            BidScraperItapitanga(),
            BidScraperAlmadina(),
            BidScraperIbicarai(),
            BidScraperUbaitaba(),
            BidScraperBarroPreto(),
            BidScraperItape()
        ]
        
        for scraper in scrapers:
            logger_main.info(f'Iniciando scraper para a cidade de {scraper._scraper_name}')
            scraper.run_script()
            logger_main.info(f'Scraper concluído para a cidade de {scraper._scraper_name}')
            run_database()
        logger_main.info('Finalizado o scraping para todos os municípios')
    except Exception as error:
        logger_main.error(f'Erro CRÍTICO encontrado durante a execução: {error}', exc_info=True) # exc_info=True informa detalhes da exceção apresentada
    finally:
        logger_main.info('Processo principal encerrado')