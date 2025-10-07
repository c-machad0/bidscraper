"""
main.py

Ponto de entrada para execução do scraping de licitações municipais.
Orquestra execução dos scrapers específicos por município e atualização do banco de dados.
"""
import schedule
import time

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
                #BidScraperItapitanga(),
                #BidScraperAlmadina(),
                #BidScraperIbicarai(),
                #BidScraperUbaitaba(),
                #BidScraperBarroPreto(),
                #BidScraperItape()
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
        schedule.every().day.at("21:26").do(self.run_app)

        self.logger_main.info('Scraper sendo iniciado')

        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == '__main__':
    app = Main()
    app.run_schedule()
