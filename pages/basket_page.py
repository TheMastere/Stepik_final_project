
from .base_page import BasePage
from .locators import ProductPageLocators


class BasketPage(BasePage):
    def not_message_about_add_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADDED_BASKET), "No message about product in basket"

    def message_about_add_basket_is_present(self):
        assert not self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_EMPTY), "No message about basket is empty"