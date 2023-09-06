from selenium.webdriver.support import expected_conditions as EC
import contextlib

class element_to_be_present_either_of_two_conditions(object):
    def __init__(self, locator1, locator2):
        self.locator1 = locator1
        self.locator2 = locator2

    def __call__(self, driver):
        with contextlib.suppress(Exception):
            element1 = EC.presence_of_element_located(self.locator1)(driver)
            return ('first', element1)
        with contextlib.suppress(Exception):
            element2 = EC.presence_of_element_located(self.locator2)(driver)
            return ('second', element2)
        return False
