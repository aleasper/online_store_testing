from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math

class BasePage(object):
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, search_method, element):
        try:
            self.browser.find_element(search_method, element)
        except (NoSuchElementException):
            return False
        return True

    # this method solves math problem from browser alert
    # use parameter "?promo=newYear" to see it
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
