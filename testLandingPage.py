from utility import *

# preferences-------------------------------------------------------------------

# Ordered sequence of columns in rows.
# Must start with Feature (3) as of now.
# The idea is that this list should be the only thing you need to change
# when testing various Home Page configurations. But for now it must start with Text Block (3)
# Feel free to add/delete/move other columns and rows
# Just make sure the column widths of each row sum to 3
column_sequence = [
'Text Block (3)', # This must come first
'Single Promo',
'Promo Row (3)',
'Video',
'News Listing'
]


# upload a sample image to your Wordpress media
# library and use this keyword to search for it
sample_image_keyword = '1280'





# helpers-----------------------------------------------------------------------

def fill_news_listing():
    form = get_active_element()
    api = config.get('API Sources', 'news_listing')
    form.send_keys('Recent News', Keys.TAB, 'http://placekitten.com', Keys.TAB, api, Keys.TAB)

def fill_promo_row():
    form = get_active_element()
    for sec in range(3):
        form.send_keys(li.get_sentence(), Keys.TAB, li.get_sentence(), Keys.TAB,
        'http://placekitten.com', Keys.TAB, li.get_sentence(), Keys.TAB)
        form = get_active_element()

def fill_single_promo():
    form = get_active_element()
    form.send_keys(li.get_sentence(), Keys.TAB, li.get_sentence(), Keys.TAB,
        'http://placekitten.com', Keys.TAB, li.get_sentence(), Keys.TAB)

def fill_text_block():
    iframes = browser.find_elements_by_tag_name('iframe')
    for frame in iframes:
        if frame.is_displayed():
            frame.click()
            frame.send_keys(li.get_sentences(3), Keys.TAB)
            break


def fill_video():
    form = get_active_element()
    form.send_keys('https://www.youtube.com/watch?v=dMH0bHeiRNg', Keys.TAB,
        li.get_sentence(), Keys.TAB, li.get_sentence(), Keys.TAB)





# create landing page -------------------------------------------------------------
def test_landing_page():
    # new page
    browser.get('https://aerodev.engin.umich.edu/wp-admin/post-new.php?post_type=page')

    print 'Building a Landing Page...'

    # select template
    browser.find_element_by_xpath("//select[@id='page_template']/option[text()='Landing Page']").click()

    # enter title
    browser.find_element_by_id('title').send_keys(li.get_sentence())

    # find and save bottom-most Add Row button
    add_row =  None
    add_row_elems = browser.find_elements_by_link_text("Add Row")
    for elem in reversed(add_row_elems):
        if elem.is_displayed():
            add_row = elem
            break

    # remove admin bar that sometimes hides elements
    browser.execute_script("document.getElementById('wpadminbar').style.display = 'none';")

    add_row.click()

    # add rows
    for row in range(len(column_sequence)):



        # find and click bottom-most Add Column(s) button
        add_col_elems = browser.find_elements_by_link_text("Add Column(s)")
        for add_col in reversed(add_col_elems):
            if add_col.is_displayed():
                add_col.click()
                break

        browser.find_element_by_link_text(column_sequence[row]).click()
        browser.find_element_by_id('footer-upgrade').click() # click away
        add_row.click()

    # extend Promo Row to be 3 units long
    for elem in browser.find_elements_by_link_text("Add Row"):
        if elem.is_displayed() and elem != add_row:
            for x in range(2):
                elem.click()

    # populate info
    dispatcher = {
    'Promo Row (3)' : fill_promo_row,
    'Video' : fill_video,
    'Single Promo' : fill_single_promo,
    'News Listing' : fill_news_listing,
    'Text Block (3)' : fill_text_block
    }

    print 'Writing lots of content...'
    for index in range(len(column_sequence)):
        dispatcher[column_sequence[index]]()


    # add images
    print 'Adding some photos...'
    add_image_buttons = browser.find_elements_by_link_text("Add Image")
    for add_image in add_image_buttons:
        if add_image.is_displayed():
            add_image.click()
            time.sleep(1.5)
            media_tab = browser.find_element_by_link_text("Media Library")
            media_tab.click()
            search = browser.find_element_by_id('media-search-input')
            search.send_keys(sample_image_keyword)
            time.sleep(4)
            search.click()
            search.send_keys(Keys.TAB, Keys.ENTER)
            browser.find_element_by_css_selector('.button.media-button.button-primary.button-large.media-button-select').click()

    # preview
    print 'Generating preview...'
    preview = browser.find_element_by_id('post-preview')
    time.sleep(1)
    preview.click()
    browser.switch_to_window(browser.window_handles[1])

    # load content
    WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, "header")))

    # take screenshot
    screenshot_and_save(time.strftime("landingPage-%Y%m%d-%H%M%S.png"))
