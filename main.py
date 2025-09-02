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



class BidScraper:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.download_dir = os.path.join(BASE_DIR, 'downloads')

        os.makedirs(self.download_dir, exist_ok=True) # Cria a pasta, caso não esteja criada

        self.options = Options()
        prefs = {
            'download.default_directory': self.download_dir,
            'download.prompt_for_download': False
        }

        self.options.add_experimental_option('prefs', prefs)
        self.service = ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

    def access_url(self):
        raise NotImplementedError

    def key_search(self, search_term):
        search = self.driver.find_elements(By. ID, 'search')
        field = search[4]
        field.send_keys(search_term) # Pregão Eletrônico

    def button_search(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > app-root > app-licitacoes > div.content-i > div.content-box.mt-0 > div:nth-child(6) > div > form > div > div.col-sm-4.mt-4 > button.btn.btn-primary'))
        )

        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)

        try:
            button.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", button)

    def json_icon(self):
        json_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-licitacoes/div[1]/div[3]/div[5]/div/div[2]/button[4]/img'))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", json_button)

        try:
            json_button.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", json_button)

    def download_file(self):
        timeout = 30
        start_time = time.time()
        while True:
            files = os.listdir(self.download_dir)
            still_downloading = any(file.startswith('.crdownload') or file.endswith('.tmp') for file in files)

            if not still_downloading:
                print('Nenhum arquivo .crdownload ou .tmp encontrado. Download finalizado!')
                break

            if time.time() - start_time > timeout:
                print('Tempo limite atingido! Ainda pode estar baixando')
                break

            time.sleep(1)

    def custom_file(self):
        raise NotImplementedError

    def print_file(self):
        folderpath = self.download_dir
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
        self.driver.quit()

class BidScraperItajuipe(BidScraper):
    def access_url(self):
        self.driver.get('https://transparencia.itajuipe.ba.gov.br/licitacoes')

    def custom_file(self):
        current_date = date.today().strftime('%d-%m-%Y')
        new_name = f'{current_date}_itajuipe.json'

        folderpath = self.download_dir
        file_type = "*.json"
        downloaded_file = glob.glob(os.path.join(folderpath, file_type))

        if not downloaded_file:
            print('Nenhum arquivo JSON encontrado')
            return

        max_file = max(downloaded_file, key=os.path.getctime)

        old_path = os.path.join(self.download_dir, max_file)
        new_path = os.path.join(self.download_dir, new_name)

        if os.path.exists(new_path):
            os.remove(new_path)

        os.rename(old_path, new_path)

class BidScraperItapitanga(BidScraper):
    def access_url(self):
        self.driver.get('https://transparencia.itapitanga.ba.gov.br/licitacoes')

    def custom_file(self):
        current_date = date.today().strftime('%d-%m-%Y')
        new_name = f'{current_date}_itapitanga.json'

        folderpath = self.download_dir
        file_type = "*.json"
        downloaded_file = glob.glob(os.path.join(folderpath, file_type))

        if not downloaded_file:
            print('Nenhum arquivo JSON encontrado')
            return

        max_file = max(downloaded_file, key=os.path.getctime)

        old_path = os.path.join(self.download_dir, max_file)
        new_path = os.path.join(self.download_dir, new_name)

        if os.path.exists(new_path):
            os.remove(new_path)

        os.rename(old_path, new_path)

class BidScraperAlmadina(BidScraper):
    def access_url(self):
        self.driver.get('https://transparencia.almadina.ba.gov.br/licitacoes')

class BidScraperCoaraci(BidScraper):
    def access_url(self):
        self.driver.get('https://acessoainformacao.coaraci.ba.gov.br/licitacoes/')

scrapper_itajuipe = BidScraperItajuipe()
scrapper_itajuipe.access_url()
scrapper_itajuipe.key_search('Pregão Eletrônico')
scrapper_itajuipe.button_search()
scrapper_itajuipe.json_icon()
scrapper_itajuipe.download_file()
scrapper_itajuipe.custom_file()
scrapper_itajuipe.print_file()
scrapper_itajuipe.quit_driver()