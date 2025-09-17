from database import BidDatabase
from scrapers import BidScraperItajuipe, BidScraperItapitanga, BidScraperAlmadina, BidScraperIbicarai, BidScraperUbaitaba

def run_database():
    db = BidDatabase()
    db.connector
    db.create_table()
    db.update_table()
    #db.list_data()
    db.close_database()

if __name__ == '__main__':
    scrapers = [
        BidScraperItajuipe(),
        BidScraperItapitanga(),
        BidScraperAlmadina(),
        BidScraperIbicarai(),
        BidScraperUbaitaba()
    ]
    
    for scraper in scrapers:
        scraper.run_script()
        run_database()