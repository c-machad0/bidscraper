"""
messages.py

Arquivo responsável por faz a ligação entre as informações do banco de dados e
o telegram do cliente.
"""
import asyncio
from datetime import date

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

    async def _send_message_async(self, text: str):
        try:
            await self.bot_message.send_message(
                chat_id=chat_id,
                text=text,
                parse_mode='Markdown'
            )
            
        except Exception as e:
            self.message_log.error(f'Erro ao enviar mensagem: {e}')

    def send_daily_reports(self):
        info_database = self.db.list_database()
        self.db.close_database()

        current_date = date.today().strftime('%Y-%m-%d')
        messages_sent = 0

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        for row in info_database:
            extraction_date = (row[4])[:10] # [:10]pega somente os 10 primeiros caracteres da coluan (YYYY-MM-DD)
            if extraction_date == current_date:
                msg = (
                    '⚠️ Nova licitação encontrada ⚠️\n'
                    f'{"Cidade:":<12} {row[1]}\n' # imprime o texto alinhado à esquerda com espaço reservado de 12 caracteres
                    f'{"Modalidade:":<12} {row[3]}\n'
                    f'{"Resumo:":<12} {row[2]}\n'
                    f'{"Acessar Portal:":<12} {CITIES_URLS[row[1]]}'
                    )
                loop.run_until_complete(self._send_message_async(msg))
                messages_sent += 1
        
        loop.close()

        if messages_sent == 0:
            self.message_log.info('Nenhuma licitação encontrada hoje')
        else:
            self.message_log.info(f'{messages_sent} mensagens enviadas no dia de hoje ({date.today().strftime('%d-%m-%Y')})')

if __name__ == '__main__':
    sender = DailyReportSender()
    sender.send_daily_reports()