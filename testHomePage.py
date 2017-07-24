from random_words import LoremIpsum
from selenium.webdriver.common.keys import Keys
from utility import *
li = LoremIpsum()

# preferences-------------------------------------------------------------------

# ordered sequence of columns to add
# this should be mutable to allow for testing of
# various Home Page configurations
# as long as the cols of each row sum to 3
column_sequence = [
'Feature (3)',

'Promo Row (3)',

'Promo Column (1)',
'In The News Listing (1)',
'Single Promo (1)',

'Department Highlights (3)',

'Link Column (1)',
'Events (1)',
'Single Promo (1)',

'Section Title (3)',

'Video (2)',
'News Listing (1)'
]

# you can change the number of subrows that appear under sections like
# Department Highlights or Link Column
subrows = 2

#-------------------------------------------------------------------------------

def test_home_page(browser):

    def fill_feature():
        link_labels = browser.find_elements_by_xpath("//label[text()='Link']")
        for link_label in link_labels:
            if link_label.is_displayed():
                link_label.click()
                link_label.send_keys('www.placekitten.com/1280/720', Keys.TAB,
                    li.get_sentence(), Keys.TAB, li.get_sentence(), Keys.TAB,
                    li.get_sentences(2), Keys.TAB)
                break

    def fill_promo_column():
        form = get_active_element(browser)
        for sec in range(2):
            form.send_keys(li.get_sentence(), Keys.TAB, 'www.placekitten.com/1280/720',
                Keys.TAB, li.get_sentences(2), Keys.TAB, li.get_sentences(2), Keys.TAB)
            form = get_active_element(browser)

    def fill_in_the_news_listing():
        form = get_active_element(browser)
        form.send_keys('www.google.com', Keys.TAB,'www.google.com', Keys.TAB,'www.google.com', Keys.TAB)

    def fill_single_promo():
        form = get_active_element(browser)
        form.send_keys(li.get_sentence(), Keys.TAB, li.get_sentences(2), Keys.TAB,
            'www.placekitten/200/300', Keys.TAB, li.get_sentence(), Keys.TAB)

    def fill_dept_highlights():
        form = get_active_element(browser)
        form.send_keys(li.get_sentence(), Keys.TAB, li.get_sentence(), Keys.TAB,
            li.get_sentences(2), Keys.TAB, 'www.placekitten.com/350/400',
            Keys.TAB, "Click here to learn more", Keys.TAB)
        form = get_active_element(browser)
        for x in range(subrows):
            form.send_keys('Example Title', Keys.TAB, li.get_sentence(), Keys.TAB,
            'www.placekitten.com', Keys.TAB)
            form = get_active_element(browser)


    def fill_promo_row():
        form = get_active_element(browser)
        for sec in range(3):
            form.send_keys(li.get_sentence(), Keys.TAB, li.get_sentences(2), Keys.TAB,
            'www.placekitten.com/350/400', Keys.TAB, li.get_sentence(), Keys.TAB)
            form = get_active_element(browser)

    def fill_link_column():
        form = get_active_element(browser)
        form.send_keys('Just Some Links', Keys.TAB)
        form = get_active_element(browser)
        for x in range(subrows):
            form.send_keys('www.placekitten.com', Keys.TAB, li.get_sentence(), Keys.TAB)
            form = get_active_element(browser)

    def fill_events():
        form = get_active_element(browser)
        form.send_keys('Events Listing', Keys.TAB,
            'placekitten.com', Keys.TAB, 'placekitten.com', Keys.TAB)

    def fill_section_title():
        form = get_active_element(browser)
        form.send_keys('Another Section', Keys.TAB)

    def fill_video():
        form = get_active_element(browser)
        form.send_keys('https://www.youtube.com/watch?v=dMH0bHeiRNg', Keys.TAB,
            li.get_sentence(), Keys.TAB)

    def fill_news_listing():
        form = get_active_element(browser)
        form.send_keys('Recent News', Keys.TAB, 'placekitten.com', Keys.TAB,
            'placekitten.com', Keys.TAB)


    # new page
    browser.get('https://aerodev.engin.umich.edu/wp-admin/post-new.php?post_type=page')

    # select template
    browser.find_element_by_xpath("//select[@id='page_template']/option[text()='Home Page']").click()

    # enter title
    browser.find_element_by_id('title').send_keys(li.get_sentence())

    # find and save Add Row button
    add_row =  None
    add_row_elems = browser.find_elements_by_link_text("Add Row")
    for elem in add_row_elems:
        if elem.is_displayed():
            add_row = elem
            break


    cols_in_row = 0
    add_row.click()

    # add rows
    for row in range(len(column_sequence)):

        if cols_in_row is 3:
            add_row.click() # new row
            cols_in_row = 0 # reset counter


        # find and click bottom-most Add Column(s) button
        add_col = None
        add_col_elems = browser.find_elements_by_link_text("Add Column(s)")
        for elem in reversed(add_col_elems):
            if elem.is_displayed():
                add_col = elem
                break


        add_col.click()
        cols_in_row += int(column_sequence[row][-2])
        print cols_in_row
        browser.find_element_by_link_text(column_sequence[row]).click()
        browser.find_element_by_id('footer-upgrade').click() # click away


    # add subrows
    for elem in browser.find_elements_by_link_text("Add Row"):
        if elem.is_displayed() and elem != add_row:
            for x in range(subrows):
                elem.click()

    # populate info
    dispatcher = {
    'Promo Column (1)' : fill_promo_column,
    'Promo Row (3)' : fill_promo_row,
    'Link Column (1)' : fill_link_column,
    'Feature (3)' : fill_feature,
    'Department Highlights (3)' : fill_dept_highlights,
    'Video (2)' : fill_video,
    'Single Promo (1)' : fill_single_promo,
    'Events (1)' : fill_events,
    'Section Title (3)' : fill_section_title,
    'News Listing (1)' : fill_news_listing,
    'In The News Listing (1)' : fill_in_the_news_listing
    }

    for index in range(len(column_sequence)):
        dispatcher[column_sequence[index]]()
    quit()





    # TODO somehow automate adding images
    add_image_buttons = browser.find_elements_by_link_text("Add Image")
    for add_image in add_image_buttons:
        if add_image.is_displayed():
            add_image.click()
            break


    # click image
    time.sleep(1)
    browser.find_element_by_id('media-search-input').send_keys(Keys.TAB, Keys.ENTER)
    browser.find_element_by_css_selector('.button.media-button.button-primary.button-large.media-button-select').click()
