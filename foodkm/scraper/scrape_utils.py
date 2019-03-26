import os
from selenium import webdriver


def login():
    print("start extraction of product_ids")
    # Log In
    driverLocation = '/usr/local/bin/chromedriver'
    driver = webdriver.Chrome(driverLocation)
    url = "https://www.telecompra.mercadona.es/ns/principal.php"
    driver.get(url)
    aqui = driver.find_elements_by_css_selector('.marcotexto a')
    aqui[0].click()

    user = driver.find_elements_by_css_selector('#username')
    user[0].send_keys(os.environ["MERCADONA_USER"])

    passw = driver.find_elements_by_css_selector('#password')
    passw[0].send_keys(os.environ["MERCADONA_PASS"])

    submit = driver.find_elements_by_css_selector('#ImgEntradaAut')
    submit[0].click()

    return driver


def switch_to_menu(driver):
    driver.switch_to.default_content()
    driver.switch_to.frame("toc")
    driver.switch_to.frame("menu")
