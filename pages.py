from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class IndexPage:
    """Represents main page."""

    _url = "https://www.imdb.com/"
    _search_input_locator = (By.ID, "suggestion-search")

    def __init__(self, driver):
        self._driver = driver

    def visit(self):
        self._driver.get(self._url)

    def search(self, text):
        search_input = self._driver.find_element(*self._search_input_locator)
        search_input.clear()
        search_input.send_keys(text)
        search_input.send_keys(Keys.ENTER)
        return MainResultsPage(self._driver)


class MainResultsPage:
    """Represents result-page of search with narrowed sections and mixed categories e.g. movies / tv / games."""

    _movie_filter_locator = (By.LINK_TEXT, "Movie")

    def __init__(self, driver):
        self._driver = driver

    def go_to_movie_titles(self):
        movie_link = self._driver.find_element(*self._movie_filter_locator)
        movie_link.click()
        return MovieResultsPage(self._driver)


class MovieResultsPage:
    """Represents result-page of search, where we can find a list of all movies."""

    _movie_listing_locator = (By.CLASS_NAME, "findList")
    _movie_title_locator = (By.CSS_SELECTOR, ".result_text a")

    def __init__(self, driver):
        self._driver = driver

    def is_listing_empty(self):
        try:
            self._driver.find_element(*self._movie_title_locator)
        except NoSuchElementException:
            return True
        return False

    def is_phrase_in_any_movie_title(self, phrase):
        movie_listing = self._driver.find_element(*self._movie_listing_locator)
        try:
            movie_listing.find_element(By.PARTIAL_LINK_TEXT, phrase)
        except NoSuchElementException:
            return False
        return True
