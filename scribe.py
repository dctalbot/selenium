from utility import *
# from testCollegeHomepage import test_college_homepage
from testHomePage import test_home_page
from testLandingPage import test_landing_page
# import new test functions here and include them in a menu option below


# menu--------------------------------------------------------------------------
def print_menu():
    print (30 * '-')
    print ("  SCRIBE ~ A SELENIUM SCRIPT")
    print (30 * '-')
    print ("1. Generate Department Homepage")
    print ("2. Generate Department Landing Page")
    print ("3. Capture Fullpage Screnshot")
    print ("4. Quit")
    print (30 * '-' + '\n')



# driver------------------------------------------------------------------------
print "\nHello! We'll go ahead and log you into Wordpress...\n"

# print menu and prompt user
while True:
    print_menu()

    try:
        mode = int(raw_input('Enter your choice [1-5]: '))
    except ValueError:
        print "That's not a number!\n"
        continue

    # generate college site homepage
    # if mode is 1:
    #     login(config.get('Settings', 'college_login'))
    #     test_college_homepage()
    #     print 'Done!\nOk, great. Now you can make all the manual edits you want.'

    # generate deptarment homepage
    if mode is 1:
        try:
            login(config.get('Settings', 'dept_login'))
        except:
            pass
        test_home_page()
        print 'Done!\nOk, great. Now you can make all the manual edits you want.'

    # generate department landing page
    elif mode is 2:
        try:
            login(config.get('Settings', 'dept_login'))
        except:
            pass
        test_landing_page()
        print 'Done!\nOk, great. Now you can make all the manual edits you want.'

    # capture fullpage screenshot
    elif mode is 3:
        while True:
            try:
                name = raw_input("Enter a name ending in .png: ")
                assert name[-4:] == '.png'
                screenshot_and_save(name)
            except AssertionError:
                print "Include the .png extension when you name your file"
                continue
            break

    else:
        print 'Bye!'
        exit()
