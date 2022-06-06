from YandexPages import *
import pytest

"""тестовые методы по заданию 1 2"""

def test_yandex_search(set_up):
    yandex_main_page = SearchHelper(set_up)
    yandex_main_page.go_to_site()
    yandex_main_page.enter_word("Тензор")
    yandex_main_page.check_suggestion_list_is()
    yandex_main_page.click_enter()
    yandex_main_page.check_search_result()


def test_yandex_pictures(set_up):
    yandex_main_page = SearchHelper(set_up)
    yandex_main_page.go_to_site()
    yandex_main_page.check_navigation_bar("Картинки")
    yandex_main_page.click_pictures()
    yandex_main_page.select_window(1)
    yandex_main_page.check_current_url()
    yandex_main_page.names_verification_go_on_second_page()
    yandex_main_page.open_1stpic_2ndpage()
    yandex_main_page.check_pic_is_open()
    yandex_main_page.change_and_verify_pic_forward()
    yandex_main_page.change_and_verify_pic_back()
    
    



    