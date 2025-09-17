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
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager


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
        if self.nofile_alert():
            print('Encerrando execução devido alerta')
            pass
        self.download_file()
        self.custom_file()
        self.quit_driver()
        
    def nofile_alert(self):
        try:
            alert = WebDriverWait(self._driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.swal2-container.swal2-center.swal2-backdrop-show > div > div.swal2-actions > button.swal2-confirm.swal2-styled'))
            )
            alert.click()
            return True 
        except TimeoutException:# Se não aparecer dentro do timeout, não houve alerta
            return False
        
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
                print('Download finalizado!')
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

        old_path = max_file
        new_path = os.path.join(self._download_dir, new_name)

        if os.path.exists(new_path):
            os.remove(new_path)

        os.rename(old_path, new_path)
    
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
    
    def custom_file(self):
        current_date = date.today().strftime('%d-%m-%Y')
        new_name = f'{current_date}_almadina.json'

        super().custom_file(new_name)

class BidScraperIbicarai(BidScraper):
    def access_url(self):
        self._driver.get('https://transparencia.ibicarai.ba.gov.br/licitacoes')

    def custom_file(self):
        current_date = date.today().strftime('%d-%m-%Y')
        new_name = f'{current_date}_ibicarai.json'

        super().custom_file(new_name)
        
class BidScraperUbaitaba(BidScraper):
    def access_url(self):
        self._driver.get('https://transparencia.ubaitaba.ba.gov.br/licitacoes')

    def custom_file(self):
        current_date = date.today().strftime('%d-%m-%Y')
        new_name = f'{current_date}_ubaitaba.json'

        super().custom_file(new_name)