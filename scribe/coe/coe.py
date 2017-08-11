import sys
sys.path.append('..')
from utility import *
from testHomepage import test_homepage
# import new test functions here and include them in a menu option below


# menu--------------------------------------------------------------------------
def print_menu():
    print (30 * '-')
    print ("  SCRIBE ~ A SELENIUM SCRIPT")
    print (30 * '-')
    print ("0. Log In")
    print ("1. Generate CoE Homepage")
    print ("3. Capture Fullpage Screnshot")
    print ("4. Quit")
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
        mode = int(raw_input('Enter your choice [0-4]: '))
    except ValueError:
        print "That's not a number!\n"
        continue
            
    # generate coe homepage
    elif mode is 1:
        login(config.get('Settings', 'college_login'))
        test_college_homepage()
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