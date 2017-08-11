# Scribe ~ A Selenium script to automate WordPress testing

## Setup
Enter your WordPress username and password in settings.cfg

Firefox requires [geckodriver](https://github.com/mozilla/geckodriver/releases).
Chrome requires [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads).

## Run
        cd scribe
        python scribe.py -s [site]

supported --site options:
* dept
* coe

View the browser in which the script is running and move your cursor off the screen.
This prevents unwanted hover actions.

## Troubleshooting
These tests should ideally be run on a large monitor with a decent computer.
Once the script starts, move you cursor off the screen and keep the window open.

### Screenshots
Automated screenshots will come out a bit wonky. Instead, you can use a browser's built-in capability:

#### Firefox
Type this: Shift+F2 screenshot --fullpage

#### Chrome
⌘⌥I -> ⌘+Shift+M -> ⋮ -> Capture Full Size Screenshot
