# 4 Feladat: Email mező

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
driver.get("https://black-moss-0a0440e03.azurestaticapps.net/mm43.html")


# központi időzítés
def ts():
    time.sleep(1)


# gomb és beviteli mező definíciók
# def frissit():
#     driver.refresh()
#     ts()
#     input = driver.find_element_by_id('email')
#     button = driver.find_element_by_id(('submit'))


# teszadatok
alert_messages = ["", "Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes.",
                  "Kérjük, töltse ki ezt a mezőt."]
email_testdata = ['teszt@elek.hu', 'teszt@', '']

# TC1:
input = driver.find_element_by_id('email')
button = driver.find_element_by_id(('submit'))
input.send_keys(email_testdata[0])
ts()
button.click()
ts()
results = driver.find_elements_by_xpath('//div[@class="validation-error"]')
assert len(results) == 0

# TC2:
driver.refresh()
ts()
input = driver.find_element_by_id('email')
button = driver.find_element_by_id(('submit'))
input.clear()
input.send_keys(email_testdata[1])
ts()
button.click()
results = driver.find_elements_by_xpath('//div[@class="validation-error"]')
if len(results) == 1:
    assert results[0].text == alert_messages[1]

# TC3:
driver.refresh()
ts()
input = driver.find_element_by_id('email')
button = driver.find_element_by_id(('submit'))
input.clear()
input.send_keys(email_testdata[2])
button.click()
results = driver.find_elements_by_xpath('//div[@class="validation-error"]')
if len(results) == 1:
    assert results[0].text == alert_messages[2]

# ablak lezárása, memória felszabadítása
# driver.close()
# driver.quit()
