"""
database.py

Gerencia o banco SQLite para armazenamento e consulta de dados de licitações coletados.
Inclui criação, atualização, exclusão e busca filtrada.
"""

import sqlite3
import os
import json
import glob


class BidDatabase:
    """
    Classe para manipular banco SQLite dos dados de licitações.

    Métodos incluem criação de tabela, atualização via arquivos JSON,
    busca filtrada e fechamento da conexão.
    """

    def __init__(self):
        """Configura conexão, cursor e diretório de arquivos JSON para importação."""

        self.connector = sqlite3.connect('dados_licitacao.db')
        self.db_cursor = self.connector.cursor()

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self._download_dir = os.path.join(BASE_DIR, 'downloads')

    def create_table(self):
        """Cria tabela licitacoes com restrição UNIQUE para evitar duplicidade."""

        self.db_cursor.execute('''
            CREATE TABLE IF NOT EXISTS licitacoes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cidade TEXT NOT NULL,
                data_licitacao TEXT,
                numero_licitacao TEXT,
                objeto TEXT,
                modalidade TEXT,
                status TEXT,
                data_extracao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(cidade, data_licitacao, numero_licitacao)
                )
            ''')

        self.connector.commit()

    def update_table(self):
        """
        Importa dados do JSON mais recente na pasta downloads.

        Extrai nome do município do arquivo e insere registros,
        ignorando duplicatas e removendo arquivo após processamento.
        """

        folderpath = self._download_dir
        file_type = "*.json"
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

        try:
            for data in json_file:
                self.db_cursor.execute(
                    '''INSERT INTO licitacoes (cidade, data_licitacao, numero_licitacao, objeto, modalidade, status)
                    VALUES (?, ?, ?, ?, ?, ?)''',
                (city_name.capitalize(), data.get("DataLicitacao"), data.get("NumeroLicitacao"),
                data.get("Objeto"), data.get("Modalidade"), data.get("Status"))
                )

            if os.path.exists(max_file):
                os.remove(max_file) # Remove o arquivo, assim que as informações são inseridas na base de dados
            
            self.connector.commit()

        except sqlite3.IntegrityError as e: # Lançamento de erro quando ocorrerem registros duplicados
            print(f'⚠️ Registro duplicado detectado: {e}')
            os.remove(max_file)
            self.connector.commit()

    def delete_data(self): # Testando função
        """Remove todos os registros da tabela licitacoes (uso para testes)."""

        self.db_cursor.execute('''DELETE FROM licitacoes''')

        self.connector.commit()

    def filtered_search(self, keyword_object, keyword_status):
        """
        Retorna lista de registros que correspondem aos filtros aplicados.

        Args:
            keyword_object (str): filtro para o campo objeto via LIKE
            keyword_status (str): filtro para o campo status via LIKE

        Returns:
            List of tuples com os registros encontrados.
        """

        self.db_cursor.execute('SELECT * FROM licitacoes where objeto LIKE ? and status LIKE ?', (f'%{keyword_object}%', (f'%{keyword_status}%')))
        
        filtered_info = self.db_cursor.fetchall()

        return filtered_info
    
    def close_database(self):
        """Fecha cursor e conexão com banco."""
        
        self.db_cursor.close()
        self.connector.close()