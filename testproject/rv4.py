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
# két lista kigyűjtése majd összehasonlítása
# returnMatches(a, b)
# set(a) & set(b)
# [i for i, j in zip(a, b) if i == j]

list_felsorolas = driver.find_elements_by_tag_name('li')
felsorolt_varosok = []
for _ in list_felsorolas:
    felsorolt_varosok.append(_.text)
print(len(felsorolt_varosok))
print(felsorolt_varosok)




# ablak lezárása, memória felszabadítása
# driver.close()
# driver.quit()
