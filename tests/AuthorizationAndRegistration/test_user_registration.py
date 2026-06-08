import allure

from src.Pages.AutorizationAndRegistrationObjects import AuthorizationAndRegistrationUserObjects
@allure.feature('Форма регистрации и авторизации')
class TestClickabilityAndLink:
    @allure.title('Регистрация пользователя')
    def test_registration_user(self, driver):
        authorization_and_registration_user = AuthorizationAndRegistrationUserObjects(driver)
        authorization_and_registration_user.open()
        authorization_and_registration_user.max_win()

        authorization_and_registration_user.fill_all_field_and_validation_user_registration()
