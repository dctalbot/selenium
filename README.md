# Scribe ~ A Selenium script to automate Wordpress testing.

## Setup
Make sure the General Settings in settings.cfg are what you want them to be.
These include your username, password, the Wordpress Login url of the site you wish to test, and the browser e.g. Chrome.

Firefox requires the geckodriver. Chrome requires the ChromeDriver.

## Run

        python scribe.py

Once you select an option, view the browser in which the script is running and move your cursor off the screen.
This prevents unwanted hover actions.

## Troubleshooting
These tests should ideally be run on a large monitor with a decent computer.
Once the script starts, move you cursor off the screen and keep the window open.

### Screenshots
My screenshots will probably come out a bit wonky. Instead, you can use a browser's built-in capability:

#### Firefox
Type this: Shift+F2 screenshot --fullpage

#### Chrome
⌘⌥I -> ⌘+Shift+M -> ⋮ -> Capture Full Size Screenshot
