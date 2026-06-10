import random
import string
import time
import allure
from src.SupportFunctions.WaitFunctions.wait_until_on_xpath import wait_xpath_element
from src.Pages.AutorizationAndRegistrationObjects import AuthorizationAndRegistrationUserObjects

class CartObjects:
    def __init__(self, driver):
        #1-Для запуска браузера:
        self.driver = driver
        self.MAIN_PAGE_URL = "https://intershop4.skillbox.ru/cart/"
        #2-Элементы навигационного меню:
        self.CART_ITEM = "(//a[contains(text(),'Корзина')])[1]"
        #3-Все элементы корзины:
        #Кнопки:
        self.REMOVE_PRODUCT_BUTTON = "//a[normalize-space()='×']"
        self.APPLY_COUPON_CODE_BUTTON = "//button[contains(text(),'Применить купон')]"
        self.PLACE_ORDER_BUTTON = "//a[contains(text(),'Оформить заказ')]"
        #Поля ввода:
        self.PRODUCT_AMOUNT = "//input[@id='quantity_6a28a824760ac']"
        self.COUPON_FIELD = "//input[@id='coupon_code']"
        #Текста для валидации:
        self.VALIDATION_TEXT = "//div[@role='alert']"
        #4-Элементы карточки товара:
        #Кнопки
        self.ADD_TO_CART_BUTTON = "//button[contains(text(),'В корзину')]"
        #URL товаров для добавления в в корзину:
        self.POLO_JEANS_URL = "https://intershop4.skillbox.ru/product/newpolom/"
        self.IPAD_URL = "https://intershop4.skillbox.ru/product/ipad-2020-32gb-wi-fi/"
        self.BQ_PHONE_URL = "https://intershop4.skillbox.ru/product/2%d1%81%d0%bc%d0%b0%d1%80%d1%82%d1%84%d0%be%d0%bd-bq-6430l-aurora/"

    #1-Запуск браузера:
    def open(self):
        with allure.step('Открыть главную страницу пиццерии https://pizzeria.skillbox.cc'):
            self.driver.get(self.MAIN_PAGE_URL)
    def max_win(self):
        self.driver.maximize_window()

    #2-3-4-Добавление товара в корзину и применение к нему купона
    def add_product_to_cart(self):
        with allure.step('Регистрация пользователя'):
            reg_page_items = AuthorizationAndRegistrationUserObjects(self.driver)
            self.driver.get("https://intershop4.skillbox.ru/register/")
            def random_username():
                username = ""
                for _ in range(13):
                    username += random.choice(string.ascii_lowercase)
                return username
            def random_email():
                email = ""
                for i in range(8):
                    email += random.choice(string.ascii_lowercase)
                return email + "@gm.de"
            wait_xpath_element(self.driver, reg_page_items.USERNAME_FIELD).send_keys(random_username())
            wait_xpath_element(self.driver, reg_page_items.EMAIL_FIELD).send_keys(random_email())
            wait_xpath_element(self.driver, reg_page_items.PASSWORD_FIELD).send_keys('1234567890-')
            wait_xpath_element(self.driver, reg_page_items.REGISTER_BUTTON).click()

        with allure.step('По URL перейти на товар "polo"'):
            self.driver.get(self.POLO_JEANS_URL)
        with allure.step('Добавить товар в корзину: '):
            wait_xpath_element(self.driver, self.ADD_TO_CART_BUTTON).click()
        with allure.step('В навигационном меню нажать пункт "КОРЗИНА" и перейти в корзину'):
            wait_xpath_element(self.driver, self.CART_ITEM).click()
        with allure.step('В поле "Введите код купона..." впишите GIVEMEHALYAVA и нажмите кнопку "ПРИМЕНИТЬ КУПОН"'):
            wait_xpath_element(self.driver, self.COUPON_FIELD).send_keys('GIVEMEHALYAVA')
            wait_xpath_element(self.driver, self.APPLY_COUPON_CODE_BUTTON).click()
        validation_text = wait_xpath_element(self.driver, self.VALIDATION_TEXT).text.lower()
        if validation_text == "Coupon code already applied!":
            assert validation_text == "Coupon code already applied!"
        elif validation_text == "Coupon code applied successfully.":
            assert validation_text == "Coupon code applied successfully." or validation_text == "Coupon code already applied!"