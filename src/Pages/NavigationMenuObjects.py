from sys import prefix

import allure
import logging.config
import logging
from src.SupportFunctions.WaitFunctions.wait_until_on_xpath import wait_xpath_element

class NavigationMenuObjects:
    def __init__(self, driver):
        #1-Для запуска браузера:
        self.driver = driver
        self.MAIN_PAGE_URL = "https://intershop4.skillbox.ru"
        #2-Все элементы навигационного меню(Главная, каталог, мой аккаунт, корзина, оформление заказа):
        self.ITEM_MAIN = "//li[@id='menu-item-26']//a[contains(text(),'Главная')]"
        self.ITEM_CATALOG = "//a[contains(text(),'Каталог')]"
        self.ITEM_MY_ACCOUNT = "//li[@id='menu-item-30']//a[contains(text(),'Мой аккаунт')]"
        self.ITEM_CART = "//li[@id='menu-item-29']//a[contains(text(),'Корзина')]"
        self.ITEM_PLACE_ORDER = "//li[@id='menu-item-31']//a[contains(text(),'Оформление заказа')]"
        #3-Список корректых URL всех элементов навигационного меню:
        self.CORRECT_URL_LIST = [
            "https://intershop4.skillbox.ru/", "https://intershop4.skillbox.ru/product-category/catalog/",
            "https://intershop4.skillbox.ru/my-account/", "https://intershop4.skillbox.ru/cart/",
            "https://intershop4.skillbox.ru/cart/" #<--- Для элемента "Оформление заказа"
        ]
    #1-Запуск браузера:
    def open(self):
        with allure.step('Открыть главную страницу пиццерии https://pizzeria.skillbox.cc'):
            self.driver.get(self.MAIN_PAGE_URL)
    def max_win(self):
        self.driver.maximize_window()
    #2-Кликабельность и валидация всех элементов в навигационном меню:
    def click_and_validate_MainItem(self):
        with allure.step('В навигационном меню нажать пункт "Главная"'):
            wait_xpath_element(self.driver, self.ITEM_MAIN).click()
            cur_url = self.driver.current_url
        with allure.step('Проверить, что URL соответствует пункту и убедиться, что URL изменился от перехода по пункту'):
            assert cur_url == self.CORRECT_URL_LIST[0]
    def click_and_validate_Catalog(self):
        with allure.step('В навигационном меню нажать пункт "Каталог"'):
            previous_url = self.driver.current_url
            wait_xpath_element(self.driver, self.ITEM_CATALOG).click()
            cur_url = self.driver.current_url
        with allure.step('Проверить, что URL соответствует пункту и убедиться, что URL изменился от перехода по пункту'):
            assert cur_url != previous_url and cur_url == self.CORRECT_URL_LIST[1]
    def click_and_validate_MyAccount(self):
        with allure.step('В навигационном меню нажать пункт "Мой аккаунт"'):
            previous_url = self.driver.current_url
            wait_xpath_element(self.driver, self.ITEM_MY_ACCOUNT).click()
            cur_url = self.driver.current_url
        with allure.step('Проверить, что URL соответствует пункту и убедиться, что URL изменился от перехода по пункту'):
            assert cur_url != previous_url and cur_url == self.CORRECT_URL_LIST[2]
    def click_and_validate_Cart(self):
        with allure.step('В навигационном меню нажать пункт "Корзина"'):
            previous_url = self.driver.current_url
            wait_xpath_element(self.driver, self.ITEM_CART).click()
            cur_url = self.driver.current_url
        with allure.step('Проверить, что URL соответствует пункту и убедиться, что URL изменился от перехода по пункту'):
            assert cur_url != previous_url and cur_url == self.CORRECT_URL_LIST[3]
    def click_and_validate_PlaceOrder(self):
        with allure.step('В навигационном меню нажать пункт "Оформление заказа"'):
            wait_xpath_element(self.driver, self.ITEM_PLACE_ORDER).click()
            cur_url = self.driver.current_url
        with allure.step('Проверить, что URL соответствует пункту и убедиться, что URL изменился от перехода по пункту'):
            assert cur_url == self.CORRECT_URL_LIST[4]