# 5 Feladat: Kakukktojás - városok

# a szükséges csomagok, modulok betöltése
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timezone, time, date
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# webdriver konfiguráció, tesztelt oldal megnyitása
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://black-moss-0a0440e03.azurestaticapps.net/rv4.html")


# központi időzítés
def ts():
    time.sleep(1)


# gomb és beviteli mező definíciók


# teszadatok


# TC1:

# TC2:

# TC3:


# ablak lezárása, memória felszabadítása
driver.close()
driver.quit()
