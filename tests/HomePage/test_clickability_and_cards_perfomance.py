import allure
from src.Pages.HomePageObjects import HomePageObjects

@allure.feature('Главная страница')
class TestClickabilityAndLink:
    @allure.story('Блок промоакций')
    @allure.title('Кликабельность и работоспособность карточек: "Книги", "Планшета", "Фотоаппараты"')
    def test_clickability_of_links(self, driver):
        home_page = HomePageObjects(driver)
        home_page.open()
        home_page.max_win()

        home_page.click_and_validate_promotions_books()
        home_page.click_and_validate_promotions_pads()
        home_page.click_and_validate_promotions_cameras()