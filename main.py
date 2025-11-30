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
    def __init__(self, callback=None):
        self.logger_main = Loggers().get_logger('main')
        self.sender = DailyReportSender()
        self.callback = callback  # ✨ NOVO: Para enviar status para interface

    def run_app(self):
        try:
            scrapers = [
                BidScraperItajuipe(),
                BidScraperItapitanga(),
                BidScraperAlmadina(),
                BidScraperIbicarai(),
                BidScraperUbaitaba(),
                BidScraperBarroPreto(),
                BidScraperItape(),
                BidScraperUbata()
            ]
            
            total = len(scrapers)
            for idx, scraper in enumerate(scrapers, 1):
                city = scraper._scraper_name
                
                # ✨ NOVO: Notificar interface do progresso
                if self.callback:
                    self.callback('progress', {
                        'current': idx,
                        'total': total,
                        'city': city,
                        'status': 'Iniciando scraping...'
                    })
                
                self.logger_main.info(f'Iniciando scraper para a cidade de {city}')
                scraper.run_script()
                self.logger_main.info(f'Scraper concluído para a cidade de {city}')
                
                # ✨ NOVO: Notificar conclusão
                if self.callback:
                    self.callback('progress', {
                        'current': idx,
                        'total': total,
                        'city': city,
                        'status': 'Concluído!'
                    })
                
                self.run_database()

            self.logger_main.info('Finalizado o scraping para todos os municípios')
            
            # ✨ NOVO: Notificar antes de enviar mensagens
            if self.callback:
                self.callback('sending', {'status': 'Enviando notificações Telegram...'})
            
            messages_count = self.sender.send_daily_reports()
            
            # ✨ NOVO: Notificar conclusão total
            if self.callback:
                self.callback('complete', {
                    'messages_sent': messages_count,
                    'status': 'Processo concluído com sucesso!'
                })

        except Exception as error:
            self.logger_main.error(f'Erro CRÍTICO encontrado durante a execução: {error}', exc_info=True)
            
            # ✨ NOVO: Notificar erro
            if self.callback:
                self.callback('error', {'message': str(error)})
        
        finally:
            self.logger_main.info('Processo principal encerrado')
            if not self.callback:  # Só sai se não for modo interface
                sys.exit(0)
            
    def run_database(self):
        db = BidDatabase()
        db.create_table()
        db.update_table()
        db.close_database()

if __name__ == '__main__':
    app = Main()
    app.run_app()
