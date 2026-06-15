import random
import string
import allure
from src.SupportFunctions.WaitFunctions.wait_until_on_xpath import wait_xpath_element

class AuthorizationAndRegistrationUserObjects:
    def __init__(self, driver):
        #1-Для запуска браузера:
        self.driver = driver
        self.REGISTRATION_AND_AUTHORIZATION_PAGE_URL = "https://intershop4.skillbox.ru/register/"
        #2-Поля "Имя пользователя*", "Адрес почты*", "Пароль*"
        self.USERNAME_FIELD = "//input[@id='reg_username']"
        self.EMAIL_FIELD = "//input[@id='reg_email']"
        self.PASSWORD_FIELD = "//input[@id='reg_password']"
        #2-Кнопка "Зарегистрироваться"
        self.REGISTER_BUTTON = "//button[contains(text(),'Зарегистрироваться')]"
        #2-Для валидации: сообщение об успешной регистрации пользователя
        self.SUCCESSFUL_REGISTRATION = "//div[contains(text(),'Регистрация завершена')]"

    #1-Запуск браузера:
    def open(self):
        with allure.step('Открыть главную страницу intershop4 https://intershop4.skillbox.ru'):
            self.driver.get(self.REGISTRATION_AND_AUTHORIZATION_PAGE_URL)
    def max_win(self):
        self.driver.maximize_window()
    #2-Регистрация пользователя и валидация регистрации:
    def fill_all_field_and_validation_user_registration(self):
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

        wait_xpath_element(self.driver, self.USERNAME_FIELD).send_keys(random_username())
        wait_xpath_element(self.driver, self.EMAIL_FIELD).send_keys(random_email())
        wait_xpath_element(self.driver, self.PASSWORD_FIELD).send_keys('1234567890-')
        wait_xpath_element(self.driver, self.REGISTER_BUTTON).click()

        success_registration_text = wait_xpath_element(self.driver, self.SUCCESSFUL_REGISTRATION).text
        assert success_registration_text == "Регистрация завершена"