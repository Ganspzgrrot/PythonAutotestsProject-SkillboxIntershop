import allure
from src.Pages.CartObjects import CartObjects

@allure.feature('Корзина')
class TestClickabilityAndLink:
    @allure.story('Система применения промокодов')
    @allure.title('Применение купона GIVEMEHALYAVA с 20% скидкой к товарам')
    def test_apply_coupon_and_applying_a_discount(self, driver):
        cart = CartObjects(driver)
        cart.open()
        cart.max_win()

        cart.add_product_to_cart()
