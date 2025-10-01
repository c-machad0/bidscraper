"""
config.py

Arquivo onde serão armazenadas as configurações essenciais da aplicação
"""

IMPORTANT_KEYWORDS = {
    'dispensa': ['aviso de dispensa', 'aviso de contratação direta'],
    'pregão eletrônico': ['aviso de licitação pregão eletrônico', 'aviso de licitação pregão eletronico'],
    'pregão presencial': ['aviso de licitação pregão presencial', 'aviso de licitação pregao presencial'],
    'concorrência pública': ['aviso de concorrência pública', 'aviso de concorrência eletrônica']
}

CITIES_URLS = {
    'Itajuipe': 'https://diario.itajuipe.ba.gov.br/homepage',
    'Itapitanga': 'https://diario.itapitanga.ba.gov.br/homepage',
    'Almadina': 'https://diario.almadina.ba.gov.br/homepage',
    'Ibicarai': 'https://diario.ibicarai.ba.gov.br/homepage',
    'Ubaitaba': 'https://diario.ubaitaba.ba.gov.br/homepage',
    'Barropreto': 'https://diario.barropreto.ba.gov.br/homepage',
    'Itape': 'https://diario.itape.ba.gov.br/homepage'
}

SCRAP_ARGUMENTS = {
    'Headless': '--headless',
    'GPU': '--disable-gpu',
    'Sandbox': '--no-sandbox',
    'DevSHM': '--disable-dev-shm-usage'
}