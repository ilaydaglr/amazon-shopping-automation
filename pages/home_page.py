from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    """Page class representing the Amazon home page."""

    URL = "https://www.amazon.com.tr/"
    HOME_PAGE_TAB_TITLE = "Amazon.com.tr"
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")

    def go_to_homepage(self):
        """
        Navigates to the Amazon homepage.
        :return: None
        """
        self.go_to_url(self.URL)

    def is_homepage_displayed(self):
        """
        Checks if the Amazon homepage is displayed by verifying the tab title.
        :return: True if the title matches, False otherwise.
        """
        current_title = self.get_title()
        return self.HOME_PAGE_TAB_TITLE in current_title


    def search_product(self, product_to_search):
        """
        Searches for the defined product in the search box and presses Enter.
        :param product_to_search: The name of the product to search for.
        :return: None
        """
        self.send_text(*self.SEARCH_BOX, product_to_search + Keys.ENTER)