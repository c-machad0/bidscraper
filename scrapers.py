"""
scrapers.py

Contém classes para automação via Selenium do scraping dos portais de transparência.
Inclui classes base e especializadas para cada município monitorado.
"""

import os
import time
from datetime import date
import glob


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager

from config import CITIES_URLS, SCRAP_ARGUMENTS
from logger import Loggers

class BidScraper:
    """
    Classe base para scraping usando Selenium dos portais municipais.

    Responsável pela configuração do driver, navegação, download do arquivo JSON,
    renomeação do arquivo e gerenciamento do ciclo do navegador.
    """
    
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
        
        for arg in SCRAP_ARGUMENTS: # Opções utilizadas quando o servidor estiver online
            self.options.add_argument(SCRAP_ARGUMENTS[arg])

        self._service = ChromeService(ChromeDriverManager().install())
        self._driver = webdriver.Chrome(service=self._service, options=self.options)

        self.scrap_logger = Loggers().get_logger('scrapers')

    def run_script(self):
        """
        Executa sequência principal de scraping:
        1. Acessa a URL
        2. Clica no ícone para download do JSON
        3. Aguarda download
        4. Renomeia arquivo
        5. Fecha driver
        """
        
        self.access_url()
        self.json_icon()
        self.download_file()
        self.custom_file()
        self.quit_driver()
        
    def access_url(self):
        """Método abstrato para acessar a URL do portal da cidade. Deve ser implementado nas subclasses."""

        raise NotImplementedError

    def json_icon(self):
        try:
            """Encontra o botão do JSON e clica para iniciar o download."""
            json_button = WebDriverWait(self._driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#edicoesAnteriores > form > div > div.col-sm-12.mt-4 > button:nth-child(2)'))
            )
            self._driver.execute_script("arguments[0].scrollIntoView(true);", json_button)

            try:
                json_button.click()
            except (ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException):
                self._driver.execute_script("arguments[0].click();", json_button)
        
        except Exception as error:
            self.scrap_logger.error(f'{error}: Erro ao encontrar botão', exc_info=True)

    def download_file(self):
        """
        Aguarda até o download do arquivo JSON terminar, monitorando arquivos temporários na pasta.
        """

        try:
            timeout = 30
            start_time = time.time()
            while True:
                files = os.listdir(self._download_dir)
                file_downloading = any(file.startswith('.crdownload') or file.endswith('.tmp') for file in files)

                if not file_downloading:
                    self.scrap_logger.info('Download finalizado!')
                    break
                
                if time.time() - start_time > timeout:
                    self.scrap_logger.warning('Tempo de download excedido')
                    break

                time.sleep(1)
        except Exception as error:
            self.scrap_logger.warning(f'{error}: Erro inesperado', exc_info=True)

    def custom_file(self, new_name):
        """
        Renomeia o arquivo JSON baixado para new_name, removendo o antigo se existir.

        Args:
            new_name (str): novo nome para o arquivo JSON.
        """

        folderpath = self._download_dir
        file_type = "*.json"
        downloaded_file = glob.glob(os.path.join(folderpath, file_type))

        if not downloaded_file:
            self.scrap_logger.warning('Nenhum arquivo JSON encontrado')
            return
        
        max_file = max(downloaded_file, key=os.path.getctime)

        old_path = max_file
        new_path = os.path.join(self._download_dir, new_name)

        if os.path.exists(new_path):
            os.remove(new_path)

        os.rename(old_path, new_path)
    
    def quit_driver(self):
        """Fecha o driver do Selenium."""

        self._driver.quit()

class BidScraperItajuipe(BidScraper):
    _scraper_name = 'Itajuípe'

    def access_url(self):
        self._driver.get(CITIES_URLS['Itajuípe'])

    def custom_file(self):
        current_date = date.today().strftime('%d-%m-%Y')
        new_name = f'{current_date}_itajuipe.json'

        super().custom_file(new_name)

class BidScraperItapitanga(BidScraper):
    _scraper_name = 'Itapitanga'

    def access_url(self):
        self._driver.get(CITIES_URLS['Itapitanga'])

    def custom_file(self):
        current_date = date.today().strftime('%d-%m-%Y')
        new_name = f'{current_date}_itapitanga.json'

        super().custom_file(new_name)
class BidScraperAlmadina(BidScraper):
    _scraper_name = 'Almadina'

    def access_url(self):
        self._driver.get(CITIES_URLS['Almadina'])
    
    def custom_file(self):
        current_date = date.today().strftime('%d-%m-%Y')
        new_name = f'{current_date}_almadina.json'

        super().custom_file(new_name)

class BidScraperIbicarai(BidScraper):
    _scraper_name = 'Ibicaraí'

    def access_url(self):
        self._driver.get(CITIES_URLS['Ibicaraí'])

    def custom_file(self):
        current_date = date.today().strftime('%d-%m-%Y')
        new_name = f'{current_date}_ibicarai.json'

        super().custom_file(new_name)
        
class BidScraperUbaitaba(BidScraper):
    _scraper_name = 'Ubaitaba'

    def access_url(self):
        self._driver.get(CITIES_URLS['Ubaitaba'])

    def custom_file(self):
        current_date = date.today().strftime('%d-%m-%Y')
        new_name = f'{current_date}_ubaitaba.json'

        super().custom_file(new_name)

class BidScraperBarroPreto(BidScraper):
    _scraper_name = 'Barro Preto'

    def access_url(self):
        self._driver.get(CITIES_URLS['Barro Preto'])

    def custom_file(self):
        current_date = date.today().strftime('%d-%m-%Y')
        new_name = f'{current_date}_barropreto.json'

        super().custom_file(new_name)

class BidScraperItape(BidScraper):
    _scraper_name = 'Itapé'

    def access_url(self):
        self._driver.get(CITIES_URLS['Itapé'])

    def custom_file(self):
        current_date = date.today().strftime('%d-%m-%Y')
        new_name = f'{current_date}_itape.json'
        return super().custom_file(new_name)