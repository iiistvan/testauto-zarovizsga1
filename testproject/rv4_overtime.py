# 5 Feladat: Kakukktojás - városok

# a szükséges csomagok, modulok betöltése
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# webdriver konfiguráció, tesztelt oldal megnyitása
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://black-moss-0a0440e03.azurestaticapps.net/rv4.html")


# központi időzítés
def ts():
    time.sleep(1)


# TC1:
# városok gyűjtése a felsorolásból, abc sorba rendezés
list_felsorolas = driver.find_elements_by_tag_name('li')
felsorolt_varosok = []
for _ in list_felsorolas:
    felsorolt_varosok.append(_.text)
# print(len(felsorolt_varosok))
felsorolt_varosok = sorted(felsorolt_varosok)
# print(felsorolt_varosok)

# városok gyűjtése a textarea területről, abc sorba rendezés
textarea = driver.find_element_by_id('cites').text
# print(textarea)
text1 = textarea.replace(' "', '').replace('"', '')
# print(text1)
texta = text1.split(',')
texta = sorted(texta)
# print(len(texta))
# print(texta)

# a két lista különbségének vizsgálata léptetéssel
for e, v in enumerate(felsorolt_varosok):
    if felsorolt_varosok[e] != texta[e]:
        varos = texta[e]
        break
    else:
        varos = texta[-1]
print(varos)

# találat bevitele, ellenőrzés
driver.find_element_by_id('missingCity').send_keys(varos)
ts()
driver.find_element_by_id('submit').click()
assert driver.find_element_by_id('result').text == 'Eltaláltad.'

# ablak lezárása, memória felszabadítása
driver.close()
driver.quit()
