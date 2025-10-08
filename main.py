"""
main.py

Ponto de entrada para execução do scraping de licitações municipais.
Orquestra execução dos scrapers específicos por município e atualização do banco de dados.
"""
import schedule
import time
import os
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
            self.logger_main.error(f'Erro CRÍTICO encontrado durante a execução: {error}', exc_info=True) # exc_info=True informa detalhes da exceção apresentada
        
        finally:
            self.logger_main.info('Processo principal encerrado')
            sys.exit(0) # Para Railway
            
    def run_database(self):
        """
        Cria conexão com o banco, cria tabela se necessário, atualiza dados a partir de arquivos JSON
        e encerra conexão.
        """
        db = BidDatabase()
        db.create_table()
        db.update_table()
        db.clear_dispensa()
        db.close_database()

    def run_schedule(self):
        schedule.every().day.at("13:30").do(self.run_app)
        self.logger_main.info('Agendamento iniciado - execução diária às 13:30')

        while True:
            schedule.run_pending()
            time.sleep(30)

if __name__ == '__main__':
    # Para desenvolvimento local
    if os.getenv('ENVIRONMENT') == 'development':
        app = Main()
        app.run_app()
    else:
    # Para produção
        app = Main()
        app.run_schedule()