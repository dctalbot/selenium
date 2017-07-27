from selenium import webdriver
from random_words import LoremIpsum
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import ConfigParser
import os
import time
from PIL import Image

li = LoremIpsum()

config = ConfigParser.ConfigParser()
config.read('settings.cfg')


chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("test-type")
# chrome_options.add_argument("start-maximized")
# chrome_options.add_argument("--js-flags=--expose-gc")
# chrome_options.add_argument("--enable-precise-memory-info")
# chrome_options.add_argument("--disable-popup-blocking")
# chrome_options.add_argument("--disable-default-apps")
chrome_options.add_argument("disable-infobars")

browser = webdriver.Firefox() if 'x' in config.get('Settings', 'browser', 1) else webdriver.Chrome(chrome_options=chrome_options)


def login():
    uniqname = config.get('Settings', 'uniqname')
    password = config.get('Settings', 'password')
    site_login = config.get('Settings', 'site_login')

    if uniqname is 'un' or password is 'pw':
        print "Please set the username and password in the configuration file."
        exit()

    browser.implicitly_wait(5) # seconds
    browser.get(site_login)
    time.sleep(1) # sometimes chrome is too fast

    # Log in
    browser.find_element_by_id('user_login').send_keys(uniqname + '@umich.edu', Keys.TAB, password, Keys.ENTER)

    # prove your humanity with this nonhuman code
    try:
        proven = browser.find_element(By.XPATH, "//form[@id='loginform']/div[2]").text
        browser.find_element_by_id('wp-submit').click()
        time.sleep(2)
        browser.find_element_by_id('user_login').send_keys(uniqname + '@umich.edu', Keys.TAB, password, Keys.ENTER)
        proven = re.findall('\d+', proven)
        toprint = 0
        for i in proven:
            toprint += int(i)
        browser.find_element_by_name('jetpack_protect_num').send_keys(toprint)
    except:
        pass

# requires that a valid input field is active
def type_sentences(num):
    try:
        li = LoremIpsum()
        get_active_element().send_keys(li.get_sentences(num))
    except:
        print "Soemthing's not right. Make sure you've selected a text field.\n"
        pass

# requires that a valid input field is active
def type_fewer_than(limit):
    try:
        li = LoremIpsum()
        get_active_element().send_keys(li.get_sentence()[:limit])
    except:
        print "Soemthing's not right. Make sure you've selected a text field.\n"
        pass

def get_active_element():
    elem = browser.switch_to.active_element
    if isinstance(elem, dict):
        elem = browser.switch_to.active_element['value']
    return elem
