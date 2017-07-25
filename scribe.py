from utility import *
from testHomePage import test_home_page
# import new test functions here and include them in a menu option below


# helpers-----------------------------------------------------------------------
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
        test_home_page()
    else:
        print 'Bye!'
        exit()
