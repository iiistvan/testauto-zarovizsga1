# 1 Feladat: Keressük a téglalap kerületét

# a szükséges csomagok, modulok betöltése
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# webdriver konfiguráció, tesztelt oldal megnyitása
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://black-moss-0a0440e03.azurestaticapps.net/x234.html")


# központi időzítés
def ts():
    time.sleep(2)


def kerulet(ax, bx):
    a.clear()
    b.clear()
    a.send_keys(ax)
    b.send_keys(bx)
    kalk.click()
    try:
        return 2 * int(ax) + 2 * int(bx)
    except:
        return 'NaN'


def eredmeny(ker):
    ts()
    result = driver.find_element_by_id('result').text
    assert result == str(ker)


# gomb és beviteli mező definíciók
a = driver.find_element_by_id('a')
b = driver.find_element_by_id('b')
kalk = driver.find_element_by_id('submit')

# TC1: Helyes kitöltés esete
eredmeny(kerulet(99, 12))

# TC2: Nem számokkal történő kitöltés
eredmeny(kerulet('kiskutya', 12))

# TC3: Üres kitöltés
eredmeny(kerulet('', ''))

# ablak lezárása, memória felszabadítása
driver.close()
driver.quit()
