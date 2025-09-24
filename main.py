"""
main.py

Ponto de entrada para execução do scraping de licitações municipais.
Orquestra execução dos scrapers específicos por município e atualização do banco de dados.
"""

from database import BidDatabase
from scrapers import BidScraperItajuipe, BidScraperItapitanga, BidScraperAlmadina, BidScraperIbicarai, BidScraperUbaitaba, BidScraperBarroPreto

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
    scrapers = [
        #BidScraperItajuipe(),
        #BidScraperItapitanga(),
        #BidScraperAlmadina(),
        #BidScraperIbicarai(),
        #BidScraperUbaitaba(),
        BidScraperBarroPreto()
    ]
    
    for scraper in scrapers:
        scraper.run_script()
        run_database()