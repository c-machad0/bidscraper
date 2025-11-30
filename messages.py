"""
messages.py

Arquivo responsável por faz a ligação entre as informações do banco de dados e
o telegram do cliente.
"""
import asyncio
from datetime import date

from telegram import Bot
from telegram.error import TelegramError, Forbidden, BadRequest

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
            result = await self.bot_message.send_message(
                chat_id=chat_id,
                text=text,
                parse_mode='Markdown'
            )
            self.message_log.info(f'Mensagem enviada com sucesso para {chat_id}')
            return result
            
        except Forbidden as e:
            self.message_log.error(f'Bot bloqueado ou sem permissão no chat {chat_id}: {e}')
        except BadRequest as e:
            self.message_log.error(f'Requisição inválida (chat_id ou formato incorreto): {e}')
        except TelegramError as e:
            self.message_log.error(f'Erro do Telegram: {e}')
        except Exception as e:
            self.message_log.error(f'Erro inesperado ao enviar mensagem: {e}', exc_info=True)

    def send_daily_reports(self):
        info_database = self.db.list_database()
        self.db.close_database()

        current_date = date.today().strftime('%Y-%m-%d')
        messages_sent = 0

        try:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            
            for col in info_database:
                extraction_date = (col[4])[:10]
                if extraction_date == current_date:
                    msg = (
                        '⚠️ Nova licitação encontrada ⚠️\n'
                        f'{"Cidade:":<12} {col[1]}\n'
                        f'{"Modalidade:":<12} {col[3]}\n'
                        f'{"Resumo:":<12} {col[2]}\n'
                        f'{"Acessar Portal:":<12} {CITIES_URLS[col[1]]}'
                    )
                    loop.run_until_complete(self._send_message_async(msg))
                    messages_sent += 1
        finally:
            loop.close()

        if messages_sent == 0:
            self.message_log.info('Nenhuma licitação encontrada hoje')
        else:
            self.message_log.info(f'{messages_sent} mensagens enviadas no dia de hoje ({date.today().strftime("%d-%m-%Y")})')
        
        return messages_sent  # ✨ NOVO: Retorna contagem

