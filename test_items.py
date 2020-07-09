import pytest
from selenium import webdriver

def test_add_to_basket_button_present(browser):
    browser.get("http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/")
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert button, "No such element exception"