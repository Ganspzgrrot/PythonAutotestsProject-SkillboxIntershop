import allure
from src.Pages.HomePageObjects import HomePageObjects

@allure.feature("Главная страница")
class TestClickabilityAndLink:
    @allure.story('Подвал сайта')
    @allure.title('Кликабельность и работоспособность всех ссылок в блоке "Страницы сайта')
    def test_clickability_of_links(self, driver):
        home_page = HomePageObjects(driver)
        home_page.open()
        home_page.max_win()

        home_page.click_and_validate_AllProducts_link()
        home_page.click_and_validate_MainPage_link()
        home_page.click_and_validate_Cart_link()
        home_page.click_and_validate_MyAccount_link()
        home_page.click_and_validate_PlacingOrder_link()
        home_page.click_and_validate_Registration_link()