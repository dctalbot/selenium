from utility import *
from cStringIO import StringIO


# preferences-------------------------------------------------------------------

# Ordered sequence of columns in rows.
# Must start with Feature (3) as of now.
# The idea is that this list should be the only thing you need to change
# when testing various Home Page configurations. But for now it must start with feature (3)
# Feel free to add/delete/move other columns and rows
# Just make sure the column widths of each row sum to 3
column_sequence = [
'Feature (3)', # This must come first

'Department Highlights (3)',

'Section Title (3)',

'Promo Row (3)',

'Events (1)',
'News Listing (1)',
'In The News Listing (1)',

'Video (2)',
'Link Column (1)',

'Promo Column (1)',
'Single Promo (1)',
'Single Promo (1)'
]

# you can also change the number of subrows that appear under
# sections like Department Highlights or Link Column
subrows = 2

# upload a sample image to your Wordpress media
# library and use this keyword to search for it
sample_image_keyword = '1280'





# helpers-----------------------------------------------------------------------

def fill_feature():
    link_labels = browser.find_elements_by_xpath("//label[text()='Link']")
    for link_label in link_labels:
        if link_label.is_displayed():
            link_label.click()
            link_label = get_active_element()
            link_label.send_keys('http://placekitten.com', Keys.TAB,
                li.get_sentence(), Keys.TAB, li.get_sentence(), Keys.TAB,
                li.get_sentence(), Keys.TAB)
            break

def fill_promo_column():
    form = get_active_element()
    for sec in range(2):
        form.send_keys(li.get_sentence(), Keys.TAB, 'http://placekitten.com',
            Keys.TAB, li.get_sentence(), Keys.TAB, li.get_sentence(), Keys.TAB)
        form = get_active_element()

def fill_in_the_news_listing():
    form = get_active_element()
    api = config.get('API Sources', 'in_the_news')
    external = config.get('API Sources', 'in_the_news_external')
    form.send_keys(api, Keys.TAB, external, Keys.TAB,'http://placekitten.com', Keys.TAB)

def fill_single_promo():
    form = get_active_element()
    form.send_keys(li.get_sentence(), Keys.TAB, li.get_sentence(), Keys.TAB,
        'http://placekitten.com', Keys.TAB, li.get_sentence(), Keys.TAB)

def fill_dept_highlights():
    form = get_active_element()
    form.send_keys(li.get_sentence(), Keys.TAB, li.get_sentence(), Keys.TAB,
        li.get_sentence(), Keys.TAB, 'http://placekitten.com',
        Keys.TAB, "Click here to learn more", Keys.TAB)
    form = get_active_element()
    for x in range(subrows):
        form.send_keys('Example Title', Keys.TAB, li.get_sentence(), Keys.TAB,
        'http://placekitten.com', Keys.TAB)
        form = get_active_element()

def fill_promo_row():
    form = get_active_element()
    for sec in range(3):
        form.send_keys(li.get_sentence(), Keys.TAB, li.get_sentence(), Keys.TAB,
        'http://placekitten.com', Keys.TAB, li.get_sentence(), Keys.TAB)
        form = get_active_element()

def fill_link_column():
    form = get_active_element()
    form.send_keys('Quick Links', Keys.TAB)
    form = get_active_element()
    for x in range(subrows):
        form.send_keys('http://placekitten.com', Keys.TAB, li.get_sentence(), Keys.TAB)
        form = get_active_element()

def fill_events():
    form = get_active_element()
    api = config.get('API Sources', 'events')
    form.send_keys('Events Listing', Keys.TAB, 'http://placekitten.com', Keys.TAB, api, Keys.TAB)

def fill_section_title():
    form = get_active_element()
    form.send_keys('Another Section', Keys.TAB)

def fill_video():
    form = get_active_element()
    form.send_keys('https://www.youtube.com/watch?v=dMH0bHeiRNg', Keys.TAB,
        li.get_sentence(), Keys.TAB)

def fill_news_listing():
    form = get_active_element()
    api = config.get('API Sources', 'news_listing')
    form.send_keys('Recent News', Keys.TAB, 'http://placekitten.com', Keys.TAB, api, Keys.TAB)





# create home page -------------------------------------------------------------
def test_home_page():
    # new page
    browser.get('https://aerodev.engin.umich.edu/wp-admin/post-new.php?post_type=page')

    print 'Building a Home Page...'

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

    # remove admin bar that sometimes hides elements
    browser.execute_script("document.getElementById('wpadminbar').style.display = 'none';")

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
        cols_in_row += int(column_sequence[row][-2]) # record row width

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





# stitch together screenshots and save a fullpage screenshot -------------------
# from https://gist.github.com/fabtho/13e4a2e7cfbfde671b8fa81bbe9359fb
def homepage_screenshot(filename):
    print "Taking a screenshot and naming it " + filename + "..."
    verbose = False # manual toggle for debugging

    # from http://stackoverflow.com/questions/1145850/how-to-get-height-of-entire-document-with-javascript
    js = 'return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);'

    scrollheight = browser.execute_script(js)
    viewport_height = browser.execute_script("return window.innerHeight")



    slices = []
    offset = 0
    firstIteration = True
    while offset < scrollheight:
        if verbose:
            print "offset1:", offset

        # hide admin and nav after first screenshot
        if not firstIteration:
            browser.execute_script("document.getElementById('wpadminbar').style.display = 'none';")
            browser.execute_script("document.getElementsByTagName('header')[0].style.display = 'none';")

        browser.execute_script("window.scrollTo(0, %s);" % offset)
        time.sleep(2)
        img = Image.open(StringIO(browser.get_screenshot_as_png()))
        slices.append(img)


        viewport_height = browser.execute_script("return window.innerHeight")
        offset += (img.size[1] - viewport_height)

        firstIteration = False


        if verbose:
            print "scrollheight: ", scrollheight


    # sum heights of slices
    # final_height = 0
    # for img in slices:
    #     final_height += img.size[1]
    final_height = slices[0].size[1] * len(slices)

    screenshot = Image.new('RGB', (slices[0].size[0], final_height))
    offset = 0
    for img in slices:
        screenshot.paste(img, (0, offset))
        offset += img.size[1]

    screenshot.save(filename)

    # show admin and nav
    browser.execute_script("document.getElementById('wpadminbar').style.display = 'initial';")
    browser.execute_script("document.getElementsByTagName('header')[0].style.display = 'initial';")
