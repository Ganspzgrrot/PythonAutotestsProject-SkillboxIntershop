import allure
from src.SupportFunctions.WaitFunctions.wait_until_on_xpath import wait_xpath_element
from selenium.webdriver.common.action_chains import ActionChains
import time

class HomePageObjects:
    def __init__(self, driver):
        #1-Для запуска браузера:
        self.driver = driver
        self.MAIN_PAGE_URL = "https://intershop4.skillbox.ru"
        #2-Карточки-промоакции "Книги", "Планшеты", "Фотоаппараты":
        self.PROMOTIONS_BOOKS = "//aside[@id='accesspress_storemo-2']//a//div[@class='caption wow fadeIn']"
        self.PROMOTIONS_PADS = "//aside[@id='accesspress_storemo-3']//a//div[@class='caption wow fadeIn']"
        self.PROMOTIONS_CAMERAS = "//aside[@id='accesspress_storemo-4']//a//div[@class='caption wow fadeIn']"
        #2-Для валидации URL из промоакций в верху сайта интершоп4:
        self.CORRECT_URL_PROMOTIONS = [
            "https://intershop4.skillbox.ru/product-category/catalog/electronics/watch/",
            "https://intershop4.skillbox.ru/product-category/catalog/appliances/",
            "https://intershop4.skillbox.ru/product-category/catalog/electronics/photo_video/"
        ]
        #3-Карточка-промоакция "Уже в продаже" и кнопка "Просмотреть товар"
        self.VIEW_PRODUCT_BUTTON = "//span[contains(text(),'Просмотреть товар')]"
        self.PRODUCT_IPAD_TEXT = "//h1[normalize-space()='iPad 2020 32gb wi-fi']"
        #3-Для валидации URL из промоакции "Уже в продаже"
        self.CORRECT_URL_PROMOTION_ALREADY_IN_SALE = "https://intershop4.skillbox.ru/?product=ipad-2020-32gb-wi-fi"
        #4-Текстовые ссылки:
        self.ALL_PRODUCTS_LINK = "//a[contains(text(),'Все товары')]"
        self.MAIN_PAGE_LINK = "//li[@class='page_item page-item-39 current_page_item']//a[contains(text(),'Главная')]"
        self.CART_LINK = "//li[@class='page_item page-item-20']//a[contains(text(),'Корзина')]"
        self.MY_ACCOUNT_LINK = "//li[@class='page_item page-item-22']//a[contains(text(),'Мой аккаунт')]"
        self.PLACING_ORDER_LINK = "//li[contains(@class,'page_item page-item-24')]//a[contains(text(),'Оформление заказа')]"
        self.REGISTRATION_LINK = "//a[contains(text(),'Регистрация')]"
        #4-Для валидации URL из ссылок подвала сайта:
        self.CORRECT_URL_LINKS = [
            "https://intershop4.skillbox.ru/shop/", "https://intershop4.skillbox.ru/",
            "https://intershop4.skillbox.ru/cart/", "https://intershop4.skillbox.ru/my-account/",
            "https://intershop4.skillbox.ru/cart/", "https://intershop4.skillbox.ru/register/"
        ]

    #1-Запуск браузера:
    def open(self):
        with allure.step('Открыть главную страницу пиццерии https://pizzeria.skillbox.cc'):
            self.driver.get(self.MAIN_PAGE_URL)
    def max_win(self):
        self.driver.maximize_window()
    #2\3-Кликабельность и валидация всех промоакций в верху главной странице сайта интершоп4:
    def click_and_validate_promotions_books(self):
        with allure.step('Нажать на промоакции "Книги"'):
            previous_url = self.driver.current_url
            wait_xpath_element(self.driver, self.PROMOTIONS_BOOKS).click()
            cur_url = self.driver.current_url
        with allure.step('Проверить, что URL соответствует промоакции и убедиться, что URL изменился от перехода на промоакцию'):
            assert cur_url != previous_url and cur_url == self.CORRECT_URL_PROMOTIONS[0]
            self.driver.get(self.MAIN_PAGE_URL)
    def click_and_validate_promotions_pads(self):
        with allure.step('Нажать на промоакции "Планшеты"'):
            previous_url = self.driver.current_url
            wait_xpath_element(self.driver, self.PROMOTIONS_PADS).click()
            cur_url = self.driver.current_url
        with allure.step('Проверить, что URL соответствует промоакции и убедиться, что URL изменился от перехода по ссылке'):
            assert cur_url != previous_url and cur_url == self.CORRECT_URL_PROMOTIONS[1]
            self.driver.get(self.MAIN_PAGE_URL)
    def click_and_validate_promotions_cameras(self):
        with allure.step('Нажать на промоакции "Фотоаппараты"'):
            previous_url = self.driver.current_url
            wait_xpath_element(self.driver, self.PROMOTIONS_CAMERAS).click()
            cur_url = self.driver.current_url
        with allure.step('Проверить, что URL соответствует промоакции и убедиться, что URL изменился от перехода по ссылке'):
            assert cur_url != previous_url and cur_url == self.CORRECT_URL_PROMOTIONS[2]
    def click_and_validate_promotion_already_in_sale(self):
        actions = ActionChains(self.driver)
        with allure.step('На главной странице нажать на карточку промоакции "Уже в продаже"'):
            previous_url = self.driver.current_url
            for i in range(60):
                actions.scroll_by_amount(0, 10).perform()
                time.sleep(0.00001)
            wait_xpath_element(self.driver, self.VIEW_PRODUCT_BUTTON).click()
            validate_text = wait_xpath_element(self.driver, self.PRODUCT_IPAD_TEXT).text
            cur_url = self.driver.current_url
        with allure.step('Проверить, что URL соответствует промоакции и убедиться, что URL изменился от перехода по карточке либо кнопке промоакции'):
            assert cur_url != previous_url and cur_url == self.CORRECT_URL_PROMOTION_ALREADY_IN_SALE and validate_text == "iPad 2020 32gb wi-fi"
    #4-Кликабельность и валидация всех ссылок в подвале сайта:
    def click_and_validate_AllProducts_link(self):
        with allure.step('Нажать на ссылку "Все товары"'):
            previous_url = self.driver.current_url
            wait_xpath_element(self.driver, self.ALL_PRODUCTS_LINK).click()
            cur_url = self.driver.current_url
        with allure.step('Проверить, что URL соответствует ссылке и убедиться, что URL изменился от перехода по ссылке'):
            assert cur_url != previous_url and cur_url == self.CORRECT_URL_LINKS[0]
            self.driver.get(self.MAIN_PAGE_URL)
    def click_and_validate_MainPage_link(self):
        with allure.step('Нажать на ссылку "Главная"'):
            wait_xpath_element(self.driver, self.MAIN_PAGE_LINK).click()
            cur_url = self.driver.current_url
        with allure.step('Проверить, что URL соответствует ссылке и убедиться, что URL изменился от перехода по ссылке'):
            assert cur_url == self.CORRECT_URL_LINKS[1]
    def click_and_validate_Cart_link(self):
        with allure.step('Нажать на ссылку "Корзина"'):
            previous_url = self.driver.current_url
            wait_xpath_element(self.driver, self.CART_LINK).click()
            cur_url = self.driver.current_url
        with allure.step('Проверить, что URL соответствует ссылке и убедиться, что URL изменился от перехода по ссылке'):
            assert previous_url != cur_url and cur_url == self.CORRECT_URL_LINKS[2]
            self.driver.get(self.MAIN_PAGE_URL)
    def click_and_validate_MyAccount_link(self):
        with allure.step('Нажать на ссылку "Мой аккаунт"'):
            previous_url = self.driver.current_url
            wait_xpath_element(self.driver, self.MY_ACCOUNT_LINK).click()
            cur_url = self.driver.current_url
        with allure.step('Проверить, что URL соответствует ссылке и убедиться, что URL изменился от перехода по ссылке'):
            assert cur_url != previous_url and cur_url == self.CORRECT_URL_LINKS[3]
            self.driver.get(self.MAIN_PAGE_URL)
    def click_and_validate_PlacingOrder_link(self):
        with allure.step('Нажать на ссылку "Оформление заказа"'):
            previous_url = self.driver.current_url
            wait_xpath_element(self.driver, self.PLACING_ORDER_LINK).click()
            cur_url = self.driver.current_url
        with allure.step('Проверить, что URL соответствует ссылке и убедиться, что URL изменился от перехода по ссылке'):
            assert cur_url != previous_url and cur_url == self.CORRECT_URL_LINKS[4]
            self.driver.get(self.MAIN_PAGE_URL)
    def click_and_validate_Registration_link(self):
        with allure.step('Нажать на промоакции "Фотоаппараты"'):
            previous_url = self.driver.current_url
            wait_xpath_element(self.driver, self.REGISTRATION_LINK).click()
            cur_url = self.driver.current_url
        with allure.step('Проверить, что URL ссылке промоакции и убедиться, что URL изменился от перехода по ссылке'):
            assert cur_url != previous_url and cur_url == self.CORRECT_URL_LINKS[5]
            self.driver.get(self.MAIN_PAGE_URL)