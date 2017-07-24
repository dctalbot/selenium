from selenium import webdriver

def get_active_element(browser):
    elem = browser.switch_to.active_element
    if isinstance(elem, dict):
        elem = browser.switch_to.active_element['value']
    return elem
