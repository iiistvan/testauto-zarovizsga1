# 3 Feladat: Összeadó

# a szükséges csomagok, modulok betöltése
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# webdriver konfiguráció, tesztelt oldal megnyitása
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html")


# központi időzítés
def ts():
    time.sleep(1)


# operandus szerinti műveletvégzés
def count(op1, op2, op):  # source kód alapján +, -, *
    r = 0
    if op == '+':
        return int(op1) + int(op2)
    elif op == '-':
        return int(op1) - int(op2)
    elif op == '*':
        return int(op1) * int(op2)


# gomb és beviteli mező definíciók
o1 = driver.find_element_by_id('num1').text
o2 = driver.find_element_by_id('num2').text
o = driver.find_element_by_id('op').text
button = driver.find_element_by_id('submit')

button.click()
ts()
result = driver.find_element_by_id('result').text
# vizsgálat
assert str(count(o1, o2, o)) == result

# ablak lezárása, memória felszabadítása
# driver.close()
# driver.quit()
