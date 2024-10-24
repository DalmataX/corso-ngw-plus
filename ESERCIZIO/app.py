from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
import logging
import time
import os

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

firefox_driver_path = r"C:\browserdrivers\geckodriver.exe"

service = Service(firefox_driver_path)

options = Options()

PATH = r"C:\Desktop\NGW+\SELENIUM"
if not os.path.exists(PATH):
    os.makedirs(PATH)

options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.dir", PATH)
options.set_preference("browser.download.useDownloadDir", True)
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf,application/x-pdf")
options.set_preference("pdfjs.disabled", True)
options.set_preference("browser.download.manager.showWhenStarting", False)

try:
    driver = Firefox(service=service, options=options)
    driver.implicitly_wait(10)
    logging.info("Browser Firefox inizializzato")

    driver.get("https://www.arpalazio.it/")
    logging.info("Pagina principale caricata")

    try:
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "acceptcookies"))
        )
        cookie_button.click()
        logging.info("Cookie accettati con successo")
        time.sleep(2)
    except Exception as e:
        logging.warning(f"Gestione cookie: {str(e)}")

    try:
        menu_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "Servizi"))
        )
        menu_button.click()
        logging.info("Menu Servizi aperto")
        time.sleep(2)
    except Exception as e:
        logging.error(f"Errore nell'apertura del menu Servizi: {str(e)}")
        raise

    try:
        tariffario_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Tariffario"))
        )
        tariffario_link.click()
        logging.info("Cliccato su Tariffario")
        time.sleep(2)
    except Exception as e:
        logging.error(f"Errore nel cliccare Tariffario: {str(e)}")
        raise

    try:
        pdf_links = driver.find_elements(By.CSS_SELECTOR, "a[href$='.pdf']")
        documenti_scaricati = []
        
        for link in pdf_links:
            nome_file = link.text or "documento.pdf"
            try:
                link.click()
                documenti_scaricati.append(nome_file)
                logging.info(f"Scaricato documento: {nome_file}")
                time.sleep(2)
            except Exception as e:
                logging.error(f"Errore nel scaricare {nome_file}: {str(e)}")
        
        with open(os.path.join(PATH, "documenti_scaricati.txt"), "w") as f:
            for doc in documenti_scaricati:
                f.write(f"{doc}\n")
        logging.info("Lista documenti salvata con successo")

    except Exception as e:
        logging.error(f"Errore nel processo di download: {str(e)}")
        raise

except Exception as e:
    logging.error(f"Errore durante l'esecuzione: {str(e)}", exc_info=True)

finally:
    try:
        driver.quit()
        logging.info("Browser chiuso")
    except:
        logging.error("Errore nella chiusura del browser")