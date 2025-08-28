import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service = ChromeService(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)

driver.get('https://diario.itajuipe.ba.gov.br/homepage')

search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'table-filter'))
)
search.send_keys('Pregão')

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'button-table-filter'))
)
driver.execute_script("arguments[0].scrollIntoView(true);", button)

try:
    button.click()
except Exception:
    driver.execute_script("arguments[0].click();", button)

open_diario = WebDriverWait(driver, 25).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#edicoesAnteriores > div.table-responsive > table > tbody > tr:nth-child(1) > td:nth-child(4) > button.btn.btn-primary-transparent.btn-nova.btn-acoes.ms-2.ng-star-inserted > i'))
)

try:
    open_diario.click()
except Exception:
    driver.execute_script("arguments[0].scrollIntoView(true);", open_diario)
    driver.execute_script("arguments[0].click();", open_diario)

time.sleep(25)

driver.quit()