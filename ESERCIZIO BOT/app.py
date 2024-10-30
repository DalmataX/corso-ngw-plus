from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.service import Service
import time
import telebot
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_TOKEN = '7891673215:AAEmlbp-s2WyKDrpvei3qqeACtp5VIQk9RI'
bot = telebot.TeleBot(API_TOKEN)

def scrape_amazon(search_query):
    service = Service(executable_path="C:\\browserdrivers\\geckodriver.exe")
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox(service=service, options=options)
    
    try:
        driver.get(f"https://www.amazon.it/s?k={search_query.replace(' ', '+')}")
        time.sleep(2)

        products = driver.find_elements(By.XPATH, "//div[contains(@class, 's-result-item s-asin')]")
        
        if not products:
            return "Nessun prodotto trovato per la tua ricerca."
        
        results = []
        
        for product in products[:5]:
            try:
                name = product.find_element(By.XPATH, ".//span[contains(@class, 'a-text-normal')]").text
                
                try:
                    price_whole = product.find_element(By.XPATH, ".//span[@class='a-price-whole']").text
                    price_fraction = product.find_element(By.XPATH, ".//span[@class='a-price-fraction']").text
                    price = f"€{price_whole},{price_fraction}"
                except:
                    price = "Prezzo non disponibile"
                
                try:
                    reviews = product.find_element(By.XPATH, ".//span[contains(@class, 'a-size-base s-underline-text')]").text
                except:
                    reviews = "0"
        
                if name.strip():
                    results.append(f"📱 {name}\n💰 Prezzo: {price}\n⭐ Recensioni: {reviews}\n{'-' * 30}")
            
            except Exception as e:
                logger.error(f"Errore nell'estrazione dei dati: {str(e)}")
                continue
        
        if results:
            return f"🔍 Risultati per '{search_query}':\n\n" + "\n\n".join(results)
        else:
            return "Mi dispiace, non ho trovato prodotti validi per la tua ricerca."
        
    except Exception as e:
        logger.error(f"Errore durante lo scraping: {str(e)}")
        return "Si e' verificato un errore durante la ricerca. Riprova più tardi."
        
    finally:
        driver.quit()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 
                 "👋 Ciao! Sono il tuo assistente per la ricerca su Amazon.\n"
                 "Scrivimi semplicemente il nome del prodotto che vuoi cercare, "
                 "e ti mostrero' i risultati disponibili.")

@bot.message_handler(func=lambda message: True)
def search_products(message):
    search_query = message.text
    bot.reply_to(message, "🔍 Sto cercando i prodotti... attendi un momento.")
    
    try:
        results = scrape_amazon(search_query)
        bot.reply_to(message, results)
    except Exception as e:
        logger.error(f"Errore durante l'elaborazione della richiesta: {str(e)}")
        bot.reply_to(message, "Si è verificato un errore. Riprova più tardi.")

logger.info("Bot avviato e in ascolto...")
bot.infinity_polling()