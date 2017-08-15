from utility import *
from cStringIO import StringIO


# preferences-------------------------------------------------------------------

# upload a sample image to your Wordpress media
# library and use this keyword to search for it
lead_image_keyword = '1-1'
feature_image_keyword = 'feature'
community_image_keyword = 'new-lead'





# helpers-----------------------------------------------------------------------

def fill_lead():
    print "Filling out the Lead section..."
    form = get_active_element()
    form.send_keys(get_characters(55), Keys.TAB, 'http://placekitten.com', Keys.TAB)
    for link in range(4):
        form = get_active_element()
        form.send_keys(get_characters(18), Keys.TAB, 'http://placekitten.com', Keys.TAB)
    for link in range(3):
        form = get_active_element()
        form.send_keys(li.get_sentence(), Keys.TAB, li.get_sentences(2), Keys.TAB,
                        get_characters(18), Keys.TAB, 'http://placekitten.com', Keys.TAB)

def fill_feature():
    print "Filling out the Inspire + Feature section..."
    form = get_active_element()
    form.send_keys(li.get_sentence(), Keys.TAB, li.get_sentences(2), Keys.TAB)
    for link in range(2):
        form = get_active_element()
        form.send_keys(get_characters(18), Keys.TAB, 'http://placekitten.com', Keys.TAB)
    for link in range(2):
        form = get_active_element()
        form.send_keys(get_characters(30), Keys.TAB, li.get_sentences(2), Keys.TAB,
                        get_characters(18), Keys.TAB, 'http://placekitten.com', Keys.TAB)

def fill_community():
    print "Filling out the Inspire + Feature section..."
    form = get_active_element()
    form.send_keys(li.get_sentence(), Keys.TAB, li.get_sentences(2), Keys.TAB)
    for link in range(2):
        form = get_active_element()
        form.send_keys(get_characters(18), Keys.TAB, 'http://placekitten.com', Keys.TAB)
    form = get_active_element()

    form.send_keys('http://placekitten.com', Keys.TAB, li.get_sentences(2), Keys.TAB)

    for link in range(2):
        form = get_active_element()
        form.send_keys(li.get_sentences(2), Keys.TAB, 'http://placekitten.com', Keys.TAB)

    form = get_active_element()
    form.send_keys('http://placekitten.com', Keys.TAB, li.get_sentence(), Keys.TAB, 'Winston Churchill')

def add_images(keyword):
    print 'Adding some photos...'
    add_image_buttons = browser.find_elements_by_link_text("Add Image")
    for add_image in add_image_buttons:
        if add_image.is_displayed():
            add_image.click()
            time.sleep(1.5)
            media_tab = browser.find_element_by_link_text("Media Library")
            media_tab.click()
            search = browser.find_element_by_id('media-search-input')
            search.send_keys(keyword)
            time.sleep(4)
            search.click()
            search.send_keys(Keys.TAB, Keys.ENTER)
            browser.find_element_by_css_selector('.button.media-button.button-primary.button-large.media-button-select').click()


# create home page -------------------------------------------------------------
def test_homepage():
    # new page
    browser.get('https://wwwdev.engin.umich.edu/wp-admin/post-new.php?post_type=page')

    print 'Building a Homepage...'

    # select template
    browser.find_element_by_xpath("//select[@id='page_template']/option[text()='Home Page']").click()

    # enter title
    browser.find_element_by_id('title').send_keys(li.get_sentence())

    print 'Writing lots of content...'

    # fill Lead section
    browser.find_element_by_xpath("//label[text()='Lead Message']").click()
    fill_lead()
    add_images(lead_image_keyword)

    # fill Inspire + Feature section
    browser.find_element_by_link_text("Inspire + Feature").click()
    browser.find_element_by_xpath("//label[text()='Inspire (Conversion): Title']").click()
    fill_feature()
    add_images(feature_image_keyword)

    # fill Inspire + Community + Quote section
    browser.find_element_by_link_text("Inspire + Community + Quote").click()
    browser.find_element_by_xpath("//label[text()='Inspire (Community): Title']").click()
    fill_community()
    add_images(community_image_keyword)

    exit()

    # remove admin bar that sometimes hides elements
    browser.execute_script("document.getElementById('wpadminbar').style.display = 'none';")


    browser.find_element_by_id('footer-upgrade').click() # click away


    # preview
    print 'Generating preview...'
    preview = browser.find_element_by_id('post-preview')
    time.sleep(1)
    preview.click()
    browser.switch_to_window(browser.window_handles[1])

    # load content
    WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, "header")))

    # take screenshot
    try:
        screenshot_and_save(time.strftime("homepage-%Y%m%d-%H%M%S.png"))
    except:
        print "Couldn't take screenshot"
        pass
