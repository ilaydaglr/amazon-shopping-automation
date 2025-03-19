from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    """Page class representing the Amazon cart page."""

    CART_PAGE_TAB_TITLE = "Amazon.com.tr Alışveriş Sepeti"
    PRODUCT_TITLE_IN_CART = (By.CSS_SELECTOR, "span.a-truncate-cut")
    DELETE_BUTTON = (By.XPATH, "//input[@data-action='delete']")
    EMPTY_CART_MESSAGE = (By.XPATH, "//span[@id='sc-subtotal-label-activecart']")
    HOMEPAGE_LOGO = (By.ID, "nav-logo")

    def is_cart_page_displayed(self):
        """
        Verifies that the cart page is displayed by checking the tab title.
        :return: True if the cart page title matches, False otherwise.
        """
        return self.get_title() == self.CART_PAGE_TAB_TITLE

    def verify_product_in_cart(self, expected_product_title):
        """
        Verifies that the correct product is added to the cart.
        :param expected_product_title: The title of the product that was added to the cart.
        :return: True if the correct product is in the cart, False otherwise.
        """
        product_in_cart = self.wait_for_element_to_be_visible(*self.PRODUCT_TITLE_IN_CART).text
        assert expected_product_title.lower() in product_in_cart.lower(), f"Mismatch: Expected '{expected_product_title}', but found '{product_in_cart}'"
        print(f"Verified: '{expected_product_title}' is correctly added to the cart.")
        return True

    def remove_product_from_cart(self):
        """
        Clicks on the 'Delete' button to remove the product from the cart.
        :return: None
        """
        self.click(*self.DELETE_BUTTON)
        print("Product removed from cart.")

    def is_cart_empty(self):
        """
        Verifies that the cart is empty after removing the product.
        :return: True if the cart is empty, False otherwise.
        """
        return self.wait_for_element_to_be_visible(*self.EMPTY_CART_MESSAGE).is_displayed()

    def return_to_homepage(self):
        """
        Clicks on the Amazon logo to return to the homepage.
        :return: None
        """
        self.click(*self.HOMEPAGE_LOGO)