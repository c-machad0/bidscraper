import sqlite3

class BidDatabase:
    def __init__(self):
        self.connector = sqlite3.connect('dados_licitacao.db')

    def create_table(self):
        db_cursor = self.connector.cursor()

        db_cursor.execute('''
            CREATE TABLE IF NOT EXISTS licitacoes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cidade TEXT NOT NULL,
                data_licitacao TEXT,
                numero_licitacao TEXT,
                objeto TEXT,
                modalidade TEXT,
                status TEXT,
                data_extracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
                ''')

        self.connector.commit()

    def list_data(self):
        ...

    def insert_data(self):
        ...

    def update_table(self):
        ...

    def delete_data(self):
        ...


db_cursor = BidDatabase()
db_cursor.connector
db_cursor.create_table()
