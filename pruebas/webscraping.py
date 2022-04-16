from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait # esta libreria espera que la carga de sitio web este completa
from selenium.webdriver.support import expected_conditions as EC  # esta verifica si los datos existen o no 
from selenium.webdriver.common.by import By # no ayuda a escojer elementos 
from bs4 import BeautifulSoup
import time 

#opciones para la navegacion dentro de chrome
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path='C:\\Users\\Gregory Burgos\\Desktop\\PythonScraping\\Proyecto1\\chromedriver_win32\\chromedriver.exe'# ruta del driver
driver=webdriver.Chrome(driver_path, chrome_options=options)
#Iniciar en la segunda pantalla para caso de cesardevoloper
#driver.set_window_position(2000,0)
#driver.maximize_window()
#time.sleep(1)

driver.get('https://www.mercadolibre.com.do/')# para ejecutar una pagina web utilizamos drive.get
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.nav-search-input'))).send_keys('celulares')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.nav-icon-search'))).click()