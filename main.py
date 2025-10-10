"""
main.py

Ponto de entrada para execução do scraping de licitações municipais.
Orquestra execução dos scrapers específicos por município e atualização do banco de dados.
"""
import sys

from database import BidDatabase
from scrapers import (BidScraperItajuipe, BidScraperItapitanga, 
                      BidScraperAlmadina, BidScraperIbicarai, BidScraperUbaitaba, 
                      BidScraperBarroPreto, BidScraperItape, BidScraperUbata)
from logger import Loggers
from messages import DailyReportSender

class Main:
    def __init__(self):
        self.logger_main = Loggers().get_logger('main')
        self.sender = DailyReportSender()

    def run_app(self):
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
                self.logger_main.info(f'Iniciando scraper para a cidade de {scraper._scraper_name}')
                scraper.run_script()
                self.logger_main.info(f'Scraper concluído para a cidade de {scraper._scraper_name}')
                self.run_database()

            self.logger_main.info('Finalizado o scraping para todos os municípios')
            self.sender.send_daily_reports()

        except Exception as error:
            self.logger_main.error(f'Erro CRÍTICO encontrado durante a execução: {error}', exc_info=True)
        
        finally:
            self.logger_main.info('Processo principal encerrado')
            sys.exit(0)  # Necessário para Railway Cron Job
            
    def run_database(self):
        db = BidDatabase()
        db.create_table()
        db.update_table()
        db.close_database()

if __name__ == '__main__':
    # Para Railway: sempre executa o app uma vez e finaliza
    app = Main()
    app.run_app()