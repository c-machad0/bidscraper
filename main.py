from database import BidDatabase
from scrapers import BidScraperItajuipe

def run_database():
    db = BidDatabase()
    db.connector
    db.create_table()
    db.update_table()
    #db.list_data()
    db.close_database()

if __name__ == '__main__':
    scrapper_itajuipe = BidScraperItajuipe()
    scrapper_itajuipe.run_script()
    #scrapper_itapitanga = BidScraperItapitanga()
    #scrapper_itapitanga.run_script()
    #scrapper_coaraci = BidScraperCoaraci()
    #scrapper_coaraci.run_script()
    
    run_database()