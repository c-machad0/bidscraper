"""
main.py

Ponto de entrada para execução do scraping de licitações municipais.
Orquestra execução dos scrapers específicos por município e atualização do banco de dados.
"""

from database import BidDatabase
from scrapers import (BidScraperItajuipe, BidScraperItapitanga, 
                      BidScraperAlmadina, BidScraperIbicarai, BidScraperUbaitaba, 
                      BidScraperBarroPreto)
from logger import main_logger

logger = main_logger('main')

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
    logger.info('Scraper sendo iniciado')
    try:
        scrapers = [
            BidScraperItajuipe(),
            BidScraperItapitanga(),
            BidScraperAlmadina(),
            BidScraperIbicarai(),
            BidScraperUbaitaba(),
            BidScraperBarroPreto()
        ]
        
        for scraper in scrapers:
            logger.info(f'Iniciando scraper para a cidade de {scraper._scraper_name}')
            scraper.run_script()
            logger.info(f'Scraper concluído para a cidade {scraper._scraper_name}')
            run_database()
        logger.info('Finalizado o scraping para todos os municípios')
    except Exception as error:
        logger.error(f'Erro CRÍTICO encontrado durante a execução: {error}', exc_info=True) # exc_info=True informa detalhes da exceção apresentada
    finally:
        logger.info('Processo principal encerrado')