"""
messages.py

Arquivo responsável por faz a ligação entre as informações do banco de dados e
o telegram do cliente.
"""
import asyncio
import time as tm
from datetime import date

import schedule # Para agendar o envio de mensagens pelo telegram
from telegram import Bot

from database import BidDatabase
from logger import Loggers
from config import CITIES_URLS
from config_private import my_token, chat_id

class DailyReportSender:
    def __init__(self):
        self.bot_message = Bot(token=my_token)
        self.db = BidDatabase()
        self.message_log = Loggers().get_logger('messages')

    def start_schedule(self):
        schedule.every().day.at("12:57").do(self.job)

        self.message_log.info("Agendador inciado.")

        while True:
            schedule.run_pending()
            tm.sleep(1)

    async def send_message(self):
        info_database = self.db.list_database()
        current_date = date.today().strftime('%Y-%m-%d')
        messages_sent = 0
        
        for row in info_database:
            extraction_date = (row[4])[:10] # [:10]pega somente os 10 primeiros caracteres da coluan (YYYY-MM-DD)
            if extraction_date == current_date:
                await self.bot_message.send_message(
                    chat_id=chat_id,
                    text=(
                    '⚠️ Nova licitação encontrada ⚠️\n'
                    f'{"Cidade:":<12} {row[1]}\n' # imprime o texto alinhado à esquerda com espaço reservado de 12 caracteres
                    f'{"Modalidade:":<12} {row[3]}\n'
                    f'{"Resumo:":<12} {row[2]}\n'
                    f'{"Link:":<12} {CITIES_URLS[row[1]]}'
                    ),
                    parse_mode='Markdown'
                )
                messages_sent += 1
                self.message_log.info('Mensagem enviada')
        
        if messages_sent == 0:
            self.message_log.info('Nenhuma licitação encontrada hoje')

    def job(self):
        asyncio.run(self.send_message())

if __name__ == '__main__':
    sender = DailyReportSender()
    sender.start_schedule()