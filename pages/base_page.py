from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage():
    """Base class that all page models will inherit from."""

    COOKIE_POPUP_ACCEPT_BUTTON = (By.ID, "sp-cc-accept")

    def __init__(self, driver):
        """
        Initialize the BasePage with a Selenium WebDriver instance.
        :param driver: Selenium WebDriver instance.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(driver)

    def go_to_url(self, url):
        """
        Navigates to the specified URL.
        :param url: The URL to navigate to.
        :return: None
        """
        self.driver.get(url)
        self.driver.refresh() #Refreshes the page to fix when a different homepage UI opens
        self.handle_cookie_popup()

    def handle_cookie_popup(self):
        """
        Checks if the cookie popup is displayed and clicks 'Accept' to close it.
        :return: None
        """
        try:
            self.wait_for_element_to_be_visible(*self.COOKIE_POPUP_ACCEPT_BUTTON).click()
            print("Cookie pop-up closed.")
        except TimeoutException:
            print("No cookie pop-up displayed.")

    def get_title(self):
        """
        Get the title of the current page.
        :return: The title of the current page.
        """
        return self.driver.title

    def find_element(self, by, locator):
        """
        Find an element on the page.
        :param by: Locator strategy (e.g., By.ID, By.XPATH).
        :param locator: The locator value of the element.
        :return: The WebElement found.
        """
        return self.driver.find_element(by, locator)

    def wait_for_element_to_be_visible(self, by, locator, timeout = 10):
        """
        Wait for an element to be visible.
        :param by: Locator strategy (e.g., By.ID, By.XPATH).
        :param locator: The locator value of the element.
        :param timeout: Maximum wait time in seconds (default is 10).
        :return: The WebElement once it is visible.
        """
        return self.wait.until(EC.visibility_of_element_located((by, locator)))

    def wait_for_element_to_be_clickable(self, by, locator, timeout = 10):
        """
        Wait for an element to be clickable.
        :param by: Locator strategy (e.g., By.ID, By.XPATH).
        :param locator: The locator value of the element.
        :param timeout: Maximum wait time in seconds (default is 10).
        :return: The WebElement once it is clickable.
        """
        return self.wait.until(EC.element_to_be_clickable((by, locator)))

    def click(self, by, locator):
        """
        Click on an element after waiting for it to be clickable.
        :param by: Locator strategy (e.g., By.ID, By.XPATH).
        :param locator: The locator value of the element.
        :return: None
        """
        self.wait_for_element_to_be_clickable(by, locator).click()

    def send_text(self, by, locator, text):
        """
        Send text to an input field.
        :param by: Locator strategy (e.g., By.ID, By.XPATH).
        :param locator: The locator value of the element.
        :param text: The text to enter into the field.
        :return: None
        """
        self.find_element(by, locator).send_keys(text)