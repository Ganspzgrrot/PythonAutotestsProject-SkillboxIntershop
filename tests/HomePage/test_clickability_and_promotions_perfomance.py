import allure
from src.Pages.HomePageObjects import HomePageObjects

@allure.feature("Главная страница")
class TestClickabilityAndLink:
    @allure.story('Подвал сайта')
    @allure.title('Кликабельность и работоспособность карточки промоакции "Уже в продаже"')
    def test_clickability_of_links(self, driver):
        home_page = HomePageObjects(driver)
        home_page.open()
        home_page.max_win()

        home_page.click_and_validate_promotion_already_in_sale()