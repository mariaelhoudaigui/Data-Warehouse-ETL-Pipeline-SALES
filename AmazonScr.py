from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json, time

# Configuration WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
wait = WebDriverWait(driver, 10)

# Liste des URLs produits
product_urls = [
    'https://www.jumia.ma/casque-gamer-casque-pc-avec-son-surround-casque-antibruit-avec-micro-et-lumiere-led-dml-mpg1043242.html',
    'https://www.jumia.ma/disque-dur-hdd-1tb-1to-externe-1000gb-toshiba-mpg1429207.html',
    'https://www.jumia.ma/casque-gamer-casque-pc-avec-son-surround-casque-antibruit-avec-micro-et-lumiere-led-dml-mpg1043242.html',
    'https://www.jumia.ma/disque-dur-hdd-1tb-1to-externe-1000gb-toshiba-mpg1429207.html',
    'https://www.jumia.ma/3200-dpi-reglables-et-7d-led-optique-souris-de-jeu-filaire-usb-pour-gamer-pc-sh-mpg1219514.html',
    'https://www.jumia.ma/canon-jet-dencre-pixma-ts3340-mfp-wifi-64926313.html',
    'https://www.jumia.ma/adaptateur-hdmi-vga-hdmi-vert-vga-hdmi-to-vga-49524863.html',
    'https://www.jumia.ma/cle-usb-64gb-usb-pour-stockage-usb-3.2-datatraveler-exodia-kingston-mpg932956.html',
    'https://www.jumia.ma/samsung-memory-card-micro-sd-carte-memoire-micro-sdxc-classe-10-128-gb-130mbs-59758408.html',
    'https://www.jumia.ma/xiaomi-mi-router-4c-white-1-an-de-garantie-49116938.html',
    'https://www.jumia.ma/sac-a-dos-thinkpad-sac-de-voyage-manche-en-velours-grande-capacite-lenovo-mpg1443949.html'
]

# Fonction d'extraction d'évaluation
def get_average_rating(url):
    try:
        driver.get(url)
        time.sleep(3)  # attendre que la page charge
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        rating = soup.find('div', class_='-fs29 -yl5 -pvxs')  # le CSS peut changer
        if rating:
            span = rating.find('span')
            if span:
                note = span.text.strip()
                try:
                    return float(note.replace(',', '.'))  # remplacer la virgule par un point si nécessaire
                except ValueError:
                    return None
    except Exception as e:
        print(f"Erreur pour {url} : {e}")
    return None

# Extraction avec identifiants
ratings_data = []
for idx, url in enumerate(product_urls, start=1):
    rating = get_average_rating(url)
    if rating:
        print(f"Note trouvée pour {url} : {rating}")
        ratings_data.append({ "id": idx, "rating": rating })
    else:
        print(f"Aucune note trouvée pour {url}")

# Sauvegarde
with open('ratings.json', 'w', encoding='utf-8') as f:
    json.dump(ratings_data, f, ensure_ascii=False, indent=4)

driver.quit()
