from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

"""BasePage определяем базовые методы для работы с WebDriver"""
class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://yandex.ru/"


    def check_suggestion_list(self, locator,time=30):
        return WebDriverWait(self.driver,time).until(EC.visibility_of_element_located(locator),
                                                    message=f"Can't find element by locator {locator}")
    
    def find_element(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def find_clickable_element(self, locator, time=10):
        return WebDriverWait(self.driver,time).until(EC.element_to_be_clickable(locator),
                                                    message=f"Can't find element by locator {locator}")
    
    def go_to_site(self):
        return self.driver.get(self.base_url)
        
    def select_window(self, digit):
        return self.driver.switch_to.window(self.driver.window_handles[digit])

    def get_current_url(self):
        return self.driver.current_url
        
    def get_attribute_of_locator(self, locator, locator_2, time=10):
        atr = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                        message=f"Can't find elements by locator {locator}")
        return atr.get_attribute(locator_2)