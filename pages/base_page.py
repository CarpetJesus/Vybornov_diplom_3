from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from seletools.actions import drag_and_drop as seletools_drag_and_drop

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open_page(self, url):
        self.driver.get(url)

    def wait_for_url(self, url):
        self.wait.until(EC.url_to_be(url))

    def wait_for_url_contains(self, text):
        self.wait.until(EC.url_contains(text))

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_text(self, locator):
        return self.find_element(locator).text

    def is_visible(self, locator):
        try:
            self.find_element(locator)
            return True
        except:
            return False

    def wait_for_invisible(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    def drag_and_drop(self, source_locator, target_locator):
        seletools_drag_and_drop(self.driver, source_locator, target_locator)
