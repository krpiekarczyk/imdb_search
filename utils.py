import os

from selenium.webdriver import Chrome, ChromeOptions

CHROME_DRIVER_PATH = os.getenv("CHROME_DRIVER_PATH")
CHROME_HEADLESS = os.getenv("CHROME_HEADLESS") == "true"


def create_driver(maximize_window=True):
    options = ChromeOptions()
    if CHROME_HEADLESS:
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")

    driver = Chrome(CHROME_DRIVER_PATH, options=options)
    if maximize_window:
        driver.maximize_window()
    return driver
