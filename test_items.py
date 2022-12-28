import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_is_button_present(browser):
    browser.get(link)
    time.sleep(10)  #добавлено для того, чтобы Вы могли убедиться в правильности языка
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert button, "There is no button on this page"
