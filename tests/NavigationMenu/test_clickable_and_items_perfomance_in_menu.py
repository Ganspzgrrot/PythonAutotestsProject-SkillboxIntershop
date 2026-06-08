from src.Pages.NavigationMenuObjects import NavigationMenuObjects

class TestClickabilityAndLink:
    def test_clickability_of_links(self, driver):
        navigation_menu = NavigationMenuObjects(driver)
        navigation_menu.open()
        navigation_menu.max_win()

        navigation_menu.click_and_validate_MainItem()
        navigation_menu.click_and_validate_Catalog()
        navigation_menu.click_and_validate_MyAccount()
        navigation_menu.click_and_validate_Cart()
        navigation_menu.click_and_validate_PlaceOrder()