# Scribe ~ A Selenium script to automate Wordpress testing.

## Setup
Make sure the General Settings in settings.cfg are what you want them to be.
These include your username, password, the Wordpress Login url of the site you wish to test, API endpoints, browser etc.

Firefox requires [geckodriver](https://github.com/mozilla/geckodriver/releases).
Chrome requires [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads).

## Run

        python scribe.py

Once you select an option, view the browser in which the script is running and move your cursor off the screen.
This prevents unwanted hover actions.

## Troubleshooting
These tests should ideally be run on a large monitor with a decent computer.
Once the script starts, move you cursor off the screen and keep the window open.

### Screenshots
Automated screenshots might come out a bit wonky. Instead, you can use a browser's built-in capability:

#### Firefox
Type this: Shift+F2 screenshot --fullpage

#### Chrome
⌘⌥I -> ⌘+Shift+M -> ⋮ -> Capture Full Size Screenshot
