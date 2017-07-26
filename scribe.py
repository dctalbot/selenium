from utility import *
from testHomePage import test_home_page, homepage_screenshot
# import new test functions here and include them in a menu option below


# menu--------------------------------------------------------------------------
def print_menu():
    print (30 * '-')
    print ("  SCRIBE ~ A SELENIUM SCRIPT")
    print (30 * '-')
    print ("1. Type Sentences")
    print ("2. Generate Home Page")
    print ("3. Quit")
    print (30 * '-' + '\n')



# driver------------------------------------------------------------------------
print "\nHello! We'll go ahead and log you into Wordpress...\n"
login()

# print menu and prompt user
while True:
    print_menu()

    try:
        mode = int(raw_input('Enter your choice [1-3]: '))
    except ValueError:
        print "That's not a number!\n"
        continue

    # type sentences
    if mode is 1:
        while True:
            try:
                type_sentences(int(raw_input('How many? ')))
            except ValueError:
                print "That's not a number!\n"
                continue
            break

    # test home page
    elif mode is 2:
        test_home_page()
        while True:
            try:
                name = raw_input("Now we'll take a screenshot.\nEnter a name ending in .png: ")
                assert name[-4:] == '.png'
                homepage_screenshot(browser, name)
            except AssertionError:
                print "Include the .png extension when you name you file"
                continue
            break
        print 'Done!\nOk, great. Now you can make all the manual edits you want.'
    else:
        print 'Bye!'
        exit()
