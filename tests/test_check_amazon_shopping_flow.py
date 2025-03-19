import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.search_result_page import SearchResultPage

class TestCheckAmazonShoppingFlow(unittest.TestCase):
    """
    Test case steps are:

    1. Go to https://www.amazon.com.tr/
    2. Verify that you are on the home page
    3. Type 'samsung' in the search field at the top of the screen and perform search.
    4. Verify that there are results for Samsung on the page that appears.
    5. Click on the 2nd page from the search results and verify that the 2nd page is
    currently displayed on the page that opens
    6. Go to the 3rd Product page from the top
    7. Verify that you are on the product page
    8. Add the product to the cart
    9. Verify that the product has been added to the cart
    10. Go to the cart page
    11. Verify that you are on the cart page and that the correct product has been added to
    the cart
    12. Delete the product from the cart and verify that it has been deleted
    13. Return to the home page and verify that it is on the home page
    """

    product_to_search = "samsung"
    page_number = 2
    selected_product_index = 5

    def setUp(self):
        """
        Setup method to initialize the WebDriver and open the browser.
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # Page Objects
        self.home_page = HomePage(self.driver)
        self.search_result_page = SearchResultPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.cart_page = CartPage(self.driver)

    def test_check_amazon_shopping_flow(self):
        """
        Test the complete Amazon shopping flow
        """

        # 1. Go to https://www.amazon.com.tr/
        self.home_page.go_to_homepage()

        # 2. Verify that you are on the home page
        self.assertTrue(self.home_page.is_homepage_displayed(), "Homepage is not displayed!")

        # 3. Type 'samsung' in the search field at the top of the screen and perform search.
        self.home_page.search_product(self.product_to_search)

        # 4. Verify that there are results for Samsung on the page that appears.
        self.assertTrue(self.search_result_page.is_results_displayed(), "Search results are not displayed!")
        self.search_result_page.verify_searched_products(self.product_to_search)

        # 5. Click on the 2nd page from the search results and verify that the 2nd page is currently displayed on the page that opens
        self.search_result_page.go_to_next_page()
        self.search_result_page.verify_page_displayed(self.page_number)

        # 6. Go to the 3rd Product page from the top
        self.search_result_page.go_to_selected_product_page(self.selected_product_index)

        # 7. Verify that you are on the product page
        self.assertTrue(self.product_page.is_product_page_displayed(), "Product page is not displayed!")

        #Get the added to cart product title from the product page
        #This will be used to verify that the correct product has been added to the cart
        expected_product_title = self.product_page.get_product_title()

        # 8. Add the product to the cart
        self.product_page.add_to_cart()

        # 9. Verify that the product has been added to the cart
        self.assertTrue(self.product_page.is_product_added_to_cart(), "Product is not added to cart!")

        # 10. Go to the cart page
        self.product_page.go_to_cart_page()

        # 11. Verify that you are on the cart page and that the correct product has been added to the cart
        self.assertTrue(self.cart_page.verify_product_in_cart(expected_product_title), "Incorrect product in the cart!")

        # 12. Delete the product from the cart and verify that it has been deleted
        self.cart_page.remove_product_from_cart()
        self.assertTrue(self.cart_page.is_cart_empty(), "Cart is not empty!")

        # 13. Return to the home page and verify that it is on the home page
        self.cart_page.return_to_homepage()
        self.assertTrue(self.home_page.is_homepage_displayed(), "Homepage is not displayed!")

    def tearDown(self):
        """
        Cleanup method to close the browser after the test.
        """
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

















