import sqlite3
import os
import json
import glob

class BidDatabase:
    def __init__(self):
        self.connector = sqlite3.connect('dados_licitacao.db')
        self.db_cursor = self.connector.cursor()

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self._download_dir = os.path.join(BASE_DIR, 'downloads')

    def create_table(self):
        self.db_cursor.execute('''
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
        self.db_cursor.execute('''SELECT * FROM licitacoes''')

    def update_table(self):
        folderpath = self._download_dir
        file_type = "*json"
        downloaded_file = glob.glob(os.path.join(folderpath, file_type))

        if not downloaded_file:
            print('Nenhum arquivo JSON encontrado')
            return
         
        max_file = max(downloaded_file, key=os.path.getctime)

        # Extraindo nome da cidade através do arquivo JSON
        filename = os.path.basename(max_file)
        city_name = filename.split('_')[-1].replace('.json', '') # Divide a string por '_', depois pega o ultimo elemento: 'itajuipe.json' e elimina o '.json'

        with open(max_file, 'r', encoding='utf-8') as file:
            json_file = json.load(file)

        for data in json_file:
            self.db_cursor.execute(
                '''INSERT OR IGNORE INTO licitacoes (cidade, data_licitacao, numero_licitacao, objeto, modalidade, status)
                VALUES (?, ?, ?, ?, ?, ?)''',
            (city_name.capitalize(), data.get("DataLicitacao"), data.get("NumeroLicitacao"),
             data.get("Objeto"), data.get("Modalidade"), data.get("Status"))
            )

        if os.path.exists(self._download_dir):
            os.remove(max_file) # Remove o arquivo, assim que as informações são inseridas na base de dados
        
        self.connector.commit()

    def delete_data(self):
        ...

    def close_database(self):
        self.db_cursor.close()
        self.connector.close()


db_cursor = BidDatabase()
db_cursor.connector
db_cursor.create_table()
#db_cursor.list_data()
db_cursor.update_table()
db_cursor.close_database()

