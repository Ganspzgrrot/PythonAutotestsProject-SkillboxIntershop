import allure
import logging.config
import logging
from src.SupportFunctions.WaitFunctions.wait_until_on_xpath import wait_xpath_element

class HomePageObjects:
    def __init__(self, driver):
        #Для запуска браузера:
        self.driver = driver
        self.MAIN_PAGE_URL = "https://intershop4.skillbox.ru"
        #Текстовые ссылки:
        self.ALL_PRODUCTS_LINK = "//a[contains(text(),'Все товары')]"
        self.MAIN_PAGE_LINK = "//li[@class='page_item page-item-39 current_page_item']//a[contains(text(),'Главная')]"
        self.CART_LINK = "//li[@class='page_item page-item-20']//a[contains(text(),'Корзина')]"
        self.MY_ACCOUNT_LINK = "//li[@class='page_item page-item-22']//a[contains(text(),'Мой аккаунт')]"
        self.PLACING_ORDER_LINK = "//li[contains(@class,'page_item page-item-24')]//a[contains(text(),'Оформление заказа')]"
        self.REGISTRATION_LINK = "//a[contains(text(),'Регистрация')]"
        #Для валидации:
        self.CORRECT_URL = [
            "https://intershop4.skillbox.ru/shop/", "https://intershop4.skillbox.ru/",
            "https://intershop4.skillbox.ru/cart/", "https://intershop4.skillbox.ru/my-account/",
            "https://intershop4.skillbox.ru/cart/", "https://intershop4.skillbox.ru/register/"
        ]

    def open(self):
        with allure.step('Открыть главную страницу пиццерии https://pizzeria.skillbox.cc'):
            self.driver.get(self.MAIN_PAGE_URL)

    def max_win(self):
        self.driver.maximize_window()

    def click_and_validate_AllProducts_link(self):
        previous_url = self.driver.current_url
        wait_xpath_element(self.driver, self.ALL_PRODUCTS_LINK).click()
        cur_url = self.driver.current_url
        assert cur_url != previous_url and cur_url == self.CORRECT_URL[0]
        self.driver.get(self.MAIN_PAGE_URL)

    def click_and_validate_MainPage_link(self):
        wait_xpath_element(self.driver, self.MAIN_PAGE_LINK).click()
        cur_url = self.driver.current_url
        assert cur_url == self.CORRECT_URL[1]

    def click_and_validate_Cart_link(self):
        previous_url = self.driver.current_url
        wait_xpath_element(self.driver, self.CART_LINK).click()
        cur_url = self.driver.current_url
        assert previous_url != cur_url and cur_url == self.CORRECT_URL[2]
        self.driver.get(self.MAIN_PAGE_URL)

    def click_and_validate_MyAccount_link(self):
        previous_url = self.driver.current_url
        wait_xpath_element(self.driver, self.MY_ACCOUNT_LINK).click()
        cur_url = self.driver.current_url
        assert cur_url != previous_url and cur_url == self.CORRECT_URL[3]
        self.driver.get(self.MAIN_PAGE_URL)

    def click_and_validate_PlacingOrder_link(self):
        previous_url = self.driver.current_url
        wait_xpath_element(self.driver, self.PLACING_ORDER_LINK).click()
        cur_url = self.driver.current_url
        assert cur_url != previous_url and cur_url == self.CORRECT_URL[4]
        self.driver.get(self.MAIN_PAGE_URL)

    def click_and_validate_Registration_link(self):
        previous_url = self.driver.current_url
        wait_xpath_element(self.driver, self.REGISTRATION_LINK).click()
        cur_url = self.driver.current_url
        assert cur_url != previous_url and cur_url == self.CORRECT_URL[5]
        self.driver.get(self.MAIN_PAGE_URL)