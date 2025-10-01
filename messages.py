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
from config import CITIES_URLS
from config_private import my_token, chat_id

bot_message = Bot(token=my_token)
bid_filter = BidDatabase()

async def send_message():
    info_database = bid_filter.list_database()

    for row in info_database:
        if (row[4])[:10] == date.today().strftime('%Y-%m-%d'): # [:10]pega somente os 10 primeiros caracteres da coluan (YYYY-MM-DD)
            await bot_message.send_message(chat_id=chat_id,
                text=f'⚠️  Nova licitação encontrada ⚠️\n'
                f'{"Cidade:":<12} {row[1]}\n' # imprime o texto alinhado à esquerda com espaço reservado de 12 caracteres
                f'{"Modalidade:":<12} {row[3]}\n'
                f'{"Resumo:":<12} {row[2]}\n'
                f'{"Link:":<12} {CITIES_URLS[row[1]]}',
                parse_mode='Markdown'
            )

def job():
    asyncio.run(send_message())

schedule.every().day.at("22:30").do(job)

while True:
    schedule.run_pending()
    tm.sleep(1)