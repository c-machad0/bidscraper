from pprint import pprint

from database import BidDatabase

send_keyword = str(input('Envie a palavra chave para ter uma busca filtrada: '))
filter = BidDatabase()
info_filter = filter.filtered_search(send_keyword)

for line in info_filter:
    pprint(line)