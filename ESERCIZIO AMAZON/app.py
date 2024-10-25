from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.service import Service
import time

def scrape_amazon():
    service = Service(executable_path="C:\\browserdrivers\\geckodriver.exe")
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(service=service, options=options)
    
    try:
        driver.get("https://www.amazon.it")
        time.sleep(1)
        
        try:
            cookie_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "sp-cc-accept"))
            )
            cookie_button.click()
            time.sleep(1)
        except TimeoutException:
            print("Nessun popup cookies trovato")
            
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        search_box.clear()
        time.sleep(1)
        search_box.send_keys("iPhone 15 Pro")
        time.sleep(1)
        search_box.send_keys(Keys.RETURN)
        
        time.sleep(2)
        
        products = driver.find_elements(
            By.XPATH, "//div[contains(@class, 's-result-item s-asin')]"
        )
        
        product_data = []
        
        for product in products:
            try:
                name = product.find_element(
                    By.XPATH, ".//span[contains(@class, 'a-text-normal')]"
                ).text
            except:
                name = "Prodotto non trovato"
                
            try:
                price_whole = product.find_element(
                    By.XPATH, ".//span[@class='a-price-whole']"
                ).text
                try:
                    price_fraction = product.find_element(
                        By.XPATH, ".//span[@class='a-price-fraction']"
                    ).text
                    price = f"€{price_whole},{price_fraction}"
                except:
                    price = f"€{price_whole},00"
            except:
                price = "Prezzo non disponibile"
                
            try:
                description = product.find_element(
                    By.XPATH, ".//div[contains(@class, 'a-row a-size-base a-color-secondary')]"
                ).text
            except:
                description = "Descrizione non disponibile"
                
            try:
                reviews = product.find_element(
                    By.XPATH, ".//span[contains(@class, 'a-size-base s-underline-text')]"
                ).text
            except:
                reviews = "Nessuna recensione"
                
            if name != "Prodotto non trovato" and name.strip() != "":
                product_info = {
                    "nome": name,
                    "prezzo": price,
                    "descrizione": description,
                    "recensioni": reviews
                }
                product_data.append(product_info)
                
        print(f"\nTrovati {len(product_data)} prodotti:\n")
        for idx, product in enumerate(product_data, 1):
            print(f"Prodotto {idx}:")
            print(f"Nome: {product['nome']}")
            print(f"Prezzo: {product['prezzo']}")
            print(f"Descrizione: {product['descrizione']}")
            print(f"Recensioni: {product['recensioni']}")
            print("-" * 50)
            
    except Exception as e:
        print(f"Si e' verificato un errore: {str(e)}")
        
    finally:
        time.sleep(1)
        driver.quit()

scrape_amazon()