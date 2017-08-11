import argparse
import subprocess

# choices
sites = [
    "dept",
    "coe"
]

# read command line
parser = argparse.ArgumentParser()
parser.add_argument('-s', '--site', choices=sites, help="Choose a site")
args = parser.parse_args()
if not args.site:
    parser.error('No --site specified.')
site = args.site


# salutation
print "Hi!"

# route
subprocess.call(['python', site + '/' + site + '.py'])

# cheers
print "Bye!"
