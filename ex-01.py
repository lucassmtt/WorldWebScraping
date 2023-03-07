from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


ROOT = Path(__file__).absolute()
CHROME_DRIVER_PATH = ROOT.parent.parent / 'local_driver' / 'chromedriver'

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    options = ()
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('https://www.github.com/lucassmtt')

    sleep(10)
