import time
import os
from datetime import date

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
download_dir = os.path.join(BASE_DIR, 'downloads')

options = Options()
prefs = {
    'download.default_directory': download_dir, # seta a pasta para onde os downloads irão
    'download.prompt_for_download': False, # evita de aparecer warnings
}
options.add_experimental_option('prefs', prefs)

service = ChromeService(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)

driver.get('https://transparencia.itajuipe.ba.gov.br/licitacoes')

# Fazer a busca
search = driver.find_elements(By.ID, 'search')
field = search[4]
field.send_keys('Pregão Eletrônico')

# Apertar o botão
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > app-root > app-licitacoes > div.content-i > div.content-box.mt-0 > div:nth-child(6) > div > form > div > div.col-sm-4.mt-4 > button.btn.btn-primary'))
)
driver.execute_script("arguments[0].scrollIntoView(true);", button)

try:
    button.click()
except Exception:
    driver.execute_script("arguments[0].click();", button)

json_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-licitacoes/div[1]/div[3]/div[5]/div/div[2]/button[4]/img'))
)
driver.execute_script("arguments[0].scrollIntoView(true);", json_button)

try:
    json_button.click()
except Exception:
    driver.execute_script("arguments[0].click();", json_button)

timeout = 30
start_time = time.time()
while True:
    files = os.listdir(download_dir)
    still_downloading = any(file.startswith('.crdownload') or file.endswith('.tmp') for file in files)

    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    if not still_downloading:
        print('Nenhum arquivo .crdownload encontrato. Download finalizado!')
        break

    if time.time() - start_time > timeout:
        print('Tempo limite atingido! Ainda pode estar baixando')
        break

    print('Baixando...')
    time.sleep(1)

current_date = date.today().strftime('%d-%m-%Y')
new_name = f'{current_date}_itajuipe.json'

for filename in os.listdir(download_dir):
        old_path = os.path.join(download_dir, filename)
        new_path = os.path.join(download_dir, new_name)

        os.rename(old_path, new_path)

driver.quit()

print(f'Arquivos na pasta: {os.listdir(download_dir)}')