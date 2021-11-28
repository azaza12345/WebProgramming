from time import sleep
from selenium import webdriver  # импортирован WebDriver для работы с браузером
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait  # импортирован WebDriverWait для использования ожиданий

"""
    Использованы Pytest 6.2.1 и Selenium 3.141.0. 
    В файл pages.txt первой строкой передается интервал, затем построчно адреса страниц
"""


def test_web():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    arr_pages = []

    def read_file(file, arr):
        for line in file:
            arr.append(line)

    f = open('pages.txt')
    read_file(f, arr_pages)
    for i in range(1, len(arr_pages)):
        driver.get(arr_pages[i])
        sleep(int(arr_pages[0]))
