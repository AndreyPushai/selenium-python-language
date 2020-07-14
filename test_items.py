import pytest
import time
from selenium import webdriver

def test_add_to_basket_button_present(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(5)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert button, "No such element exception"