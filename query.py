"""
query.py

Interface simples CLI para consulta filtrada no banco de dados de licitações.
Solicita palavra-chave e status, exibe resultados.
"""

from pprint import pprint

from database import BidDatabase

object_filter = str(input('Envie a palavra chave para ter uma busca filtrada: '))
status_filter = str(input('Envite o status desejado: '))
bid_filter = BidDatabase()
info_filter = bid_filter.filtered_search(object_filter, status_filter)

for line in info_filter:
    pprint(line)