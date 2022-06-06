from BaseApp import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

"""YandexSeacrhLocators. 
Он будет только для хранения локаторов, атрибутов:"""


class YandexSeacrhLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")      
    LOCATOR_YANDEX_SEARCH_FIELD_2PAGE = (By.CSS_SELECTOR, ".input__control")                  
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")   
    LOCATOR_YANDEX_SUGGESTION_LIST = (By.CSS_SELECTOR, "body > div.mini-suggest__popup.mini-suggest__popup_svg_yes.mini-suggest__popup_theme_tile.mini-suggest__popup_visible")
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CSS_SELECTOR, ".services-new__list-item")
    LOCATOR_YANDEX_LISTS_CITES = (By.CSS_SELECTOR, "#search-result > .serp-item a > b")
    LOCATOR_YANDEX_PICTURES_ON_PAGE = (By.LINK_TEXT, 'Картинки')
    LOCATOR_YANDEX_PICTURE_1_CATEGORY = (By.CLASS_NAME, 'PopularRequestList-SearchText')
    LOCATOR_YANDEX_OPEN_PICTURE = (By.CLASS_NAME, "MMImageContainer")
    LOCATOR_YANDEX_CLICKABLE_PICTURE = (By.CLASS_NAME,'serp-item__preview')
    LOCATOR_YANDEX_PICTURE_WINDOW = (By.CLASS_NAME, "MMImage-Preview")
    LOCATOR_YANDEX_PICTURE_RIGHT_BUTTON = (By.CLASS_NAME,'CircleButton_type_next')
    LOCATOR_YANDEX_PICTURE_LEFT_BUTTON = (By.CLASS_NAME,'CircleButton_type_prev')
    
    
    ATTRIBUTE_OF_NAME = 'innerHTML'
    ATTRIBUTE_OF_PIC_ONSEARCH = 'value'
    ATTRIBUTE_OF_WINDOW_PIC = 'src'


"""Вспомогательные методы для работы с поиском:"""

class SearchHelper(BasePage):


    def enter_word(self, word):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field
    
    def check_suggestion_list_is(self):
        return self.check_suggestion_list(YandexSeacrhLocators.LOCATOR_YANDEX_SUGGESTION_LIST,time=30)

    def click_enter(self):
        search_enter = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD,time=10)
        search_enter.send_keys(Keys.RETURN)
        return search_enter

    def check_search_result(self):
        all_list = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_LISTS_CITES,time=10)
        items = [elem.text.strip() for elem in all_list[:1]]
        if "tensor.ru" not in items:
            raise Exception('сайта tensor.ru нет в первых 1 пунктах')
       
    def check_current_url(self):
        url = self.get_current_url()
        assert "https://yandex.ru/images" in url
        return url
        
    def check_navigation_bar(self, word):
        all_list = self.find_elements(YandexSeacrhLocators.LOCATOR_YANDEX_NAVIGATION_BAR,time=10)
        nav_bar_menu = [x.text for x in all_list]
        assert word in nav_bar_menu
        return(nav_bar_menu)
        
    def click_pictures(self):
        find_and_click = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_PICTURES_ON_PAGE,time=10)
        find_and_click.click()
        return find_and_click
        
    def open_the_first_picture(self):
        the_first_picture = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_PICTURE_1_CATEGORY, time=10)
        the_first_picture.click()
    
    def names_verification_go_on_second_page(self):
        name_of_pictures_category = self.get_attribute_of_locator(YandexSeacrhLocators.LOCATOR_YANDEX_PICTURE_1_CATEGORY, YandexSeacrhLocators.ATTRIBUTE_OF_NAME, time=10)
        #print(name_of_pictures_category)
        the_first_picture = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_PICTURE_1_CATEGORY, time=10)
        the_first_picture.click()
        name_of_pictures_category_search_field = self.get_attribute_of_locator(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD_2PAGE, YandexSeacrhLocators.ATTRIBUTE_OF_PIC_ONSEARCH, time=10)
        #print(name_of_pictures_category_search_field)
        assert name_of_pictures_category in name_of_pictures_category_search_field

    def open_1stpic_2ndpage (self):
        find_to_click = self.find_clickable_element(YandexSeacrhLocators.LOCATOR_YANDEX_CLICKABLE_PICTURE, time=10)
        return find_to_click.click()
    
    def check_pic_is_open(self):
        opened_pic = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_OPEN_PICTURE, time=10)
        verify_the_pic = opened_pic.is_displayed
        return verify_the_pic

    def change_and_verify_pic_forward(self):
        image_window_1_details = self.get_attribute_of_locator(YandexSeacrhLocators.LOCATOR_YANDEX_PICTURE_WINDOW, YandexSeacrhLocators.ATTRIBUTE_OF_WINDOW_PIC, time=10)
        click_right = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_PICTURE_RIGHT_BUTTON, time=5)
        ActionChains(self.driver).move_to_element(click_right).click().perform()
        image_window_2_details = self.get_attribute_of_locator(YandexSeacrhLocators.LOCATOR_YANDEX_PICTURE_WINDOW, YandexSeacrhLocators.ATTRIBUTE_OF_WINDOW_PIC, time=10)
        assert image_window_1_details is not image_window_2_details
        return image_window_1_details
    
    def change_and_verify_pic_back(self):
        click_left = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_PICTURE_LEFT_BUTTON, time=5)
        ActionChains(self.driver).move_to_element(click_left).click().perform()
        image_window_3_details = self.get_attribute_of_locator(YandexSeacrhLocators.LOCATOR_YANDEX_PICTURE_WINDOW, YandexSeacrhLocators.ATTRIBUTE_OF_WINDOW_PIC, time=10)
        assert image_window_3_details == SearchHelper.change_and_verify_pic_forward(self)


"""класс BasePage для веб-страницы реализуется в файле YandexPages.py"""
