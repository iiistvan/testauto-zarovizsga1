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
# list(set(temp1) - set(temp2))
# set(temp1) ^ set(temp2)

list_felsorolas = driver.find_elements_by_tag_name('li')
felsorolt_varosok = []
for _ in list_felsorolas:
    felsorolt_varosok.append(_.text)
print(len(felsorolt_varosok))
print(felsorolt_varosok)

textarea = driver.find_element_by_id('cites').text
text1 = textarea.replace('"','')

print(text1)
texta = text1.split(',')
print(texta)
# s = set(texta)
# varos = [x for x in felsorolt_varosok if x not in s]
# print(varos)
varos = list(set(felsorolt_varosok)-set(texta))
print(type(varos))
# varos1 = list(varos)
print(varos)
# driver.find_element_by_id('missingCity').send_keys(varos1[0])
# driver.find_element_by_id('submit').click

# ablak lezárása, memória felszabadítása
# driver.close()
# driver.quit()
