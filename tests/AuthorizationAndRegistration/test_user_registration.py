from src.Pages.AutorizationAndRegistrationObjects import AuthorizationAndRegistrationUserObjects

class TestClickabilityAndLink:
    def test_clickability_of_links(self, driver):
        authorization_and_registration_user = AuthorizationAndRegistrationUserObjects(driver)
        authorization_and_registration_user.open()
        authorization_and_registration_user.max_win()

        authorization_and_registration_user.fill_all_field_and_validation_user_registration()