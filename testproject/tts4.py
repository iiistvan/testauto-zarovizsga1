# 2 Feladat: Pénzfeldobás

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
driver.get("https://black-moss-0a0440e03.azurestaticapps.net/tts4.html")


# központi időzítés
def ts():
    time.sleep(1)


# gomb és beviteli mező definíciók
button = driver.find_element_by_id('submit')
fej = 0
# gombnyomások
for _ in range(100):
    button.click()
results = driver.find_elements_by_xpath('//li')
# fejszámolás :)
for f in results:
    if f.text == 'fej':
        fej += 1
# vizsgálat
try:
    print(f'A fej dobások száma: {fej}')
    assert fej > 29
except:
    print('Nem működik jól, kevesebb mint 30 fej van!')

# ablak lezárása, memória felszabadítása
# driver.close()
# driver.quit()
