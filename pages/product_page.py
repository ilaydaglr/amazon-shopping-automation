from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    """Page class representing a specific Amazon product page."""

    PRODUCT_TITLE = (By.ID, "titleSection")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")
    ADDED_TO_CART_MESSAGE = (By.XPATH, "//h1[contains(text(), 'Sepete eklendi')]")
    GO_TO_CART_BUTTON = (By.CSS_SELECTOR, "a[href='/cart?ref_=sw_gtc']")

    def is_product_page_displayed(self):
        """
        Verifies that the product page is displayed by checking the product title.
        :return: True if the product page is displayed, False otherwise.
        """
        return self.wait_for_element_to_be_visible(*self.PRODUCT_TITLE).is_displayed()

    def add_to_cart(self):
        """
        Clicks on the 'Add to Cart' button.
        :return: None
        """
        self.click(*self.ADD_TO_CART_BUTTON)

    def is_product_added_to_cart(self):
        """
        Verifies that the product has been successfully added to the cart.
        :return: True if the confirmation message is displayed, False otherwise.
        """
        return self.wait_for_element_to_be_visible(*self.ADDED_TO_CART_MESSAGE).is_displayed()

    def go_to_cart_page(self):
        """
        Clicks on the 'Go to Cart' button.
        :return: None
        """
        self.click(*self.GO_TO_CART_BUTTON)

    def get_product_title(self):
        """
        Retrieves the title of the current product.
        :return: The product title.
        """
        try:
            title_element = self.wait_for_element_to_be_visible(*self.PRODUCT_TITLE, timeout=10)
            print(f"Found Product Title: {title_element.text.strip()}")
            return title_element.text.strip()
        except TimeoutException:
            print("ERROR: Could not find product title!")
            return None
