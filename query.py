"""
query.py

Interface simples CLI para consulta filtrada no banco de dados de licitações.
Solicita palavra-chave e exibe resultados.
"""

from pprint import pprint

from database import BidDatabase

modality_filter = str(input('Envie a palavra chave para ter uma busca filtrada: '))
bid_filter = BidDatabase()
info_filter = bid_filter.filtered_search(modality_filter)

for line in info_filter:
    pprint(line)