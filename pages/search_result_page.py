from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchResultPage(BasePage):
    """Page class representing the Amazon search results page."""

    PRODUCT_TITLES = (By.XPATH, "//div[@data-component-type='s-search-result']//h2")
    NEXT_PAGE_BUTTON = (By.CSS_SELECTOR, "a.s-pagination-next")
    PAGE_INDICATOR = (By.CSS_SELECTOR, "span.s-pagination-item.s-pagination-selected")
    PRODUCT_TO_BE_SELECTED = (By.XPATH, "//div[@data-index='{}']")

    def is_results_displayed(self):
        """
        Checks if the search results are displayed.
        :return: True if products are listed, False otherwise.
        """
        self.wait_for_element_to_be_visible(*self.PRODUCT_TITLES)
        return len(self.driver.find_elements(*self.PRODUCT_TITLES)) > 0

    def get_product_titles(self):
        """
        Retrieves the titles of all displayed products.
        :return: A list of product titles.
        """
        product_elements = self.driver.find_elements(*self.PRODUCT_TITLES)
        valid_products = [] # For real search results other than sponsored products.(Non-Samsung products are displayed in sponsored products.)

        for product in product_elements:
            try:
                product.find_element(By.XPATH, "//span[contains(@class, 's-sponsored-label-info-icon')]")
            except NoSuchElementException:
                valid_products.append(product.text.strip())
        return valid_products

    def verify_searched_products(self, searched_product):
        """
        Verifies that all listed products contain the searched product.
        :param searched_product: The keyword that should be present in all product titles.
        :return: None
        """
        product_titles = self.get_product_titles()

        for title in product_titles:
            assert searched_product.title() in title.title(), f"Non-{searched_product} product found: {title}"
        print(f"All products contain '{searched_product}'.")

    def go_to_next_page(self):
        """
        Clicks on the 'Next' button to navigate to the next search results page.
        :return: None
        """
        self.click(*self.NEXT_PAGE_BUTTON)
        self.wait_for_element_to_be_visible(*self.PRODUCT_TITLES)

    def verify_page_displayed(self, page_number):
        """
        Verifies that the expected search results page is displayed using both the page indicator and URL.
        :param page_number: The expected page number to verify.
        :return: None
        """
        page_number_element = self.wait_for_element_to_be_visible(*self.PAGE_INDICATOR)
        current_page = page_number_element.text.strip()
        assert current_page == str(page_number), f"Expected page {page_number}, but found page {current_page}!"

        current_url = self.driver.current_url
        expected_param = f"page={page_number}"
        assert expected_param in current_url, f"Expected URL to contain '{expected_param}', but found '{current_url}'!"

        print(f"Page {page_number} is displayed correctly in both UI and URL.")

    def go_to_selected_product_page(self, index):
        """
        Selects a product from the search results based on the given index.
        :param index: The index of the product to select.
        :return: None
        """
        product_locator = (self.PRODUCT_TO_BE_SELECTED[0], self.PRODUCT_TO_BE_SELECTED[1].format(index))
        self.click(*product_locator)