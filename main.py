import os
import time
from datetime import date
import glob
import json
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


from database import BidDatabase


def run_database():
    db = BidDatabase()
    db.connector
    db.create_table()
    db.update_table()
    db.list_data()
    db.close_database()

class BidScraper:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self._download_dir = os.path.join(BASE_DIR, 'downloads')

        os.makedirs(self._download_dir, exist_ok=True) # Cria a pasta, caso não esteja criada

        self.options = Options()
        prefs = {
            'download.default_directory': self._download_dir,
            'download.prompt_for_download': False
        }

        self.options.add_experimental_option('prefs', prefs)
        self._service = ChromeService(ChromeDriverManager().install())
        self._driver = webdriver.Chrome(service=self._service, options=self.options)

    def run_script(self):
        self.access_url()
        self.json_icon()
        self.download_file()
        self.custom_file()
        self.print_file()
        self.quit_driver()

    def access_url(self):
        raise NotImplementedError

    def json_icon(self):
        json_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-licitacoes/div[1]/div[3]/div[5]/div/div[2]/button[4]/img'))
        )
        self._driver.execute_script("arguments[0].scrollIntoView(true);", json_button)

        try:
            json_button.click()
        except Exception:
            self._driver.execute_script("arguments[0].click();", json_button)

    def download_file(self):
        timeout = 30
        start_time = time.time()
        while True:
            files = os.listdir(self._download_dir)
            file_downloading = any(file.startswith('.crdownload') or file.endswith('.tmp') for file in files)

            if not file_downloading:
                print('Nenhum arquivo .crdownload ou .tmp encontrado. Download finalizado!')
                break
            
            if time.time() - start_time > timeout:
                print('Tempo limite atingido! Ainda pode estar baixando')
                break

            time.sleep(1)

    def custom_file(self, new_name):
        folderpath = self._download_dir
        file_type = "*.json"
        downloaded_file = glob.glob(os.path.join(folderpath, file_type))

        if not downloaded_file:
            print('Nenhum arquivo JSON encontrado')
            return

        max_file = max(downloaded_file, key=os.path.getctime)

        old_path = os.path.join(self._download_dir, max_file)
        new_path = os.path.join(self._download_dir, new_name)

        if os.path.exists(new_path):
            os.remove(new_path)

        os.rename(old_path, new_path)

    def print_file(self): # Função temporária. Só esta aqui para que eu consiga visualizar melhor os dados
        folderpath = self._download_dir
        file_type = "*.json"
        downloaded_file = glob.glob(os.path.join(folderpath, file_type))

        if not downloaded_file:
            print('Nenhum arquivo JSON encontrado')
            return

        max_file = max(downloaded_file, key=os.path.getctime) # Retorna o ultimo arquivo do diretorio

        with open(max_file, 'r', encoding='utf-8') as file:
            data_file = json.load(file)

            print()

        for data in data_file:
            pprint({
                "DataLicitacao": data.get("DataLicitacao"),
                "NumeroLicitacao": data.get("NumeroLicitacao"),
                "Objeto": data.get("Objeto"),
                "Modalidade": data.get("Modalidade"),
                "Status": data.get("Status")
            })

    def quit_driver(self):
        self._driver.quit()

class BidScraperItajuipe(BidScraper):
    def access_url(self):
        self._driver.get('https://transparencia.itajuipe.ba.gov.br/licitacoes')

    def custom_file(self):
        current_date = date.today().strftime('%d-%m-%Y')
        new_name = f'{current_date}_itajuipe.json'

        super().custom_file(new_name)

class BidScraperItapitanga(BidScraper):
    def access_url(self):
        self._driver.get('https://transparencia.itapitanga.ba.gov.br/licitacoes')

    def custom_file(self):
        current_date = date.today().strftime('%d-%m-%Y')
        new_name = f'{current_date}_itapitanga.json'

        super().custom_file(new_name)

class BidScraperAlmadina(BidScraper):
    def access_url(self):
        self._driver.get('https://transparencia.almadina.ba.gov.br/licitacoes')

class BidScraperCoaraci(BidScraper):
    def access_url(self):
        self._driver.get('https://acessoainformacao.coaraci.ba.gov.br/licitacoes/')

if __name__ == '__main__':
    scrapper_itajuipe = BidScraperItajuipe()
    scrapper_itajuipe.run_script()
    
    run_database()