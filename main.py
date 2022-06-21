from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chromedriver_path = r"../../development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(by=By.CSS_SELECTOR, value="#cookie")

def buy():
    cursor = driver.find_element(by=By.CSS_SELECTOR, value="#buyCursor b")
    grandma = driver.find_element(by=By.CSS_SELECTOR, value="#buyGrandma b")
    factory = driver.find_element(by=By.CSS_SELECTOR, value="#buyFactory b")
    mine = driver.find_element(by=By.CSS_SELECTOR, value="#buyMine b")
    shipment = driver.find_element(by=By.CSS_SELECTOR, value="#buyShipment b")
    alchemy_lab = driver.find_element(by=By.CSS_SELECTOR, value="[id='buyAlchemy lab'] b")
    portal = driver.find_element(by=By.CSS_SELECTOR, value="#buyPortal b")
    time_machine = driver.find_element(by=By.CSS_SELECTOR, value="[id='buyTime machine'] b")

    items_list = [cursor, grandma, factory, mine, shipment, alchemy_lab, portal, time_machine]
    money_int = int(driver.find_element(by=By.CSS_SELECTOR, value="#money").text.replace(",", ""))
    prices_list = [int(element.text.split(" - ")[1].replace(",", "")) for element in items_list]
    for i in range(len(prices_list)-1,-1,-1):
        if money_int > prices_list[i]:
            return items_list[i].click()

timer_on = True
timer_5s = time.time() + 5
timer_5min = time.time() + 60*5
while timer_on:
    cookie.click()
    if time.time() >= timer_5s:
        buy()
        timer_5s = time.time() + 5
    if time.time() >= timer_5min:
        timer_on = False
        statistics = driver.find_element(by=By.CSS_SELECTOR, value="#cps").text
        print(statistics)
        driver.quit()
