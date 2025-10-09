import os

# Variáveis de ambiente para Railway
my_token = os.getenv('MY_TOKEN')
my_chat_id = os.getenv('MY_CHAT_ID') 
chat_id_channel = os.getenv('CHAT_ID_CHANNEL')

# Verificação se as variáveis foram carregadas
if not my_token:
    raise ValueError("MY_TOKEN não encontrado nas variáveis de ambiente")
if not chat_id_channel:
    raise ValueError("CHAT_ID_CHANNEL não encontrado nas variáveis de ambiente")
