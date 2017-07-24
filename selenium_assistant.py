from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
from random_words import LoremIpsum
import ConfigParser
from testHomePage import *
from utility import *

# read settings.cfg~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
config = ConfigParser.ConfigParser()
config.read('settings.cfg')

browser = webdriver.Firefox() if 'x' in config.get('Settings', 'browser', 1) else webdriver.Chrome()




# functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def login():
    uniqname = config.get('Settings', 'uniqname')
    password = config.get('Settings', 'password')
    site_login = config.get('Settings', 'site_login')

    if uniqname is 'uniqname' or password is 'password':
        print "you need to change the script prefs. plz see line 12"
        exit()

    browser.implicitly_wait(5) # seconds
    browser.get(site_login)

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




def print_menu():
    print (30 * '-')
    print ("      SELENIUM ASSISTANT")
    print (30 * '-')
    print ("1. Type Sentences")
    print ("2. Test Home Page")
    print ("3. Quit")
    print (30 * '-')



def type_sentences(num):
    try:
        li = LoremIpsum()
        get_active_element(browser).send_keys(li.get_sentences(num))
    except:
        print "Soemthing's not right. Make sure you've selected a text field.\n"
        pass





# DRIVER~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
login()
while True:
    print_menu()

    try:
        mode = int(raw_input('Enter your choice [1-3] : '))
    except ValueError:
        print "That's not a number!\n"
        continue

    if mode is 1:
        try:
            type_sentences(int(raw_input('How many? ')))
        except ValueError:
            print "That's not a number!\n"
            continue
    elif mode is 2:
        test_home_page(browser)
    elif mode is 3:
        print 'Bye!'
        exit()
