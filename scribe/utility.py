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
from cStringIO import StringIO

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
browser.implicitly_wait(5) # seconds

def login(url):
    print "Logging in..."
    uniqname = config.get('Settings', 'uniqname')
    password = config.get('Settings', 'password')

    if uniqname == 'un' or password == 'pw':
        print "Please set the username and password in the configuration file."
        exit()

    # browser.implicitly_wait(5) # seconds
    browser.get(url)
    time.sleep(1) # sometimes chrome is too fast

    # click sign in with un and pw if necessary
    try:
        browser.find_element_by_link_text("Log in with username and password").click()
    except:
        pass

    # Log in
    browser.find_element_by_id('user_login').send_keys(uniqname + '@umich.edu', Keys.TAB, password, Keys.ENTER)

    # prove your humanity with this nonhuman code
    try:
        digits = browser.find_element(By.XPATH, "//form[@id='loginform']/div[2]").text
        browser.find_element_by_id('wp-submit').click()
        time.sleep(2)
        browser.find_element_by_id('user_login').send_keys(uniqname + '@umich.edu', Keys.TAB, password, Keys.ENTER)
        digits = re.findall('\d+', digits)
        answer = 0
        for i in digits:
            answer += int(i)
        browser.find_element_by_name('jetpack_protect_num').send_keys(answer)
    except:
        pass

# requires that a valid input field is active
def type_sentences(quantity):
    try:
        li = LoremIpsum()
        get_active_element().send_keys(li.get_sentences(num))
    except:
        print "Soemthing's not right. Make sure you've selected a text field.\n"
        pass

def get_characters(limit):
    return li.get_sentences(2)[:limit]

def get_active_element():
    elem = browser.switch_to.active_element
    if isinstance(elem, dict):
        elem = browser.switch_to.active_element['value']
    return elem




# requires filename has valid extension e.g. .png
def screenshot_and_save(filename):
    # from https://gist.github.com/fabtho/13e4a2e7cfbfde671b8fa81bbe9359fb
    print "Taking a screenshot and naming it " + filename + " ..."

    # from http://stackoverflow.com/questions/1145850/how-to-get-height-of-entire-document-with-javascript
    js = 'return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);'

    scrollheight = browser.execute_script(js)
    viewport_height = browser.execute_script("return window.innerHeight")

    # hide admin and nav
    try:
        browser.execute_script("document.getElementById('wpadminbar').style.display = 'none';")
        browser.execute_script("document.getElementsByTagName('header')[0].style.display = 'none';")
    except:
        pass
    
    slices = []
    offset = 0
    while offset < scrollheight:
        browser.execute_script("window.scrollTo(0, %s);" % offset)
        time.sleep(2)
        img = Image.open(StringIO(browser.get_screenshot_as_png()))
        slices.append(img)

        viewport_height = browser.execute_script("return window.innerHeight")
        offset += (img.size[1] - viewport_height)


    final_height = slices[0].size[1] * len(slices)
    trim = final_height % scrollheight

    slices[-1] = slices[-1].crop((0, trim, slices[-1].size[0], slices[0].size[1]))

    # height of slices
    final_height -= trim

    screenshot = Image.new('RGB', (slices[0].size[0], final_height))
    offset = 0
    for img in slices:
        screenshot.paste(img, (0, offset))
        offset += img.size[1]

    screenshot.save(filename)

    try:
        # show admin and nav
        browser.execute_script("document.getElementById('wpadminbar').style.display = 'initial';")
        browser.execute_script("document.getElementsByTagName('header')[0].style.display = 'initial';")
    except:
        pass
        
