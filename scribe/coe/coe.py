import sys
sys.path.append('.')
from utility import *
from testHomepage import test_homepage
# import new test functions here and include them in a menu option below


# menu--------------------------------------------------------------------------
def print_menu():
    print (30 * '-')
    print ("  SCRIBE ~ A SELENIUM SCRIPT")
    print (30 * '-')
    print ("1. Generate CoE Homepage")
    print ("2. Quit")
    print (30 * '-' + '\n')



# driver------------------------------------------------------------------------

# log in
try:
    login(config.get('Settings', 'coe_login'))
except:
    print "Couldn't log in"
    quit()

# print menu and prompt user
while True:
    print_menu()

    try:
        mode = int(raw_input('Enter your choice [1-2]: '))
    except ValueError:
        print "That's not a number!\n"
        continue
            
    # generate coe homepage
    if mode is 1:
        test_homepage()
        print 'Done!\nOk, great. Now you can make all the manual edits you want.'

    # capture fullpage screenshot
    # elif mode is 2:
    #     try:
    #         screenshot_and_save(time.strftime("coe-%Y%m%d-%H%M%S.png"))
    #     except:
    #         print "Couldn't take screenshot"
    #         continue

    else:
        exit()
