
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_product_page(self):
        product_page = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        product_page.click()

    def name_message_is_same_name_in_cart(self):
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_ADDED_BASKET), \
        'Received a message about adding an item to cart'
        name_product_on_page = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        name_product = name_product_on_page.text
        name_product_in_message = self.browser.find_element(*ProductPageLocators.NAME_FROM_MESSAGE)
        name_product_message = name_product_in_message.text
        print(f"\nname_product: {name_product} ================= name_from_message: {name_product_message}\n")
        assert name_product == name_product_message, \
        "The product name on the page does not match the product name in the message"


