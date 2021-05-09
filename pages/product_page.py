
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def go_to_product_page(self):
        product_page = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        product_page.click()
        self.browser.implicitly_wait(5)

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

    def cost_is_same_as_cost_product(self):
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_PRODUCT), \
        'Got a message with the cost of the basket'
        cost_on_product_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        cost_product = cost_on_product_page.text
        cost_product_of_the_basket = self.browser.find_element(*ProductPageLocators.PRICE_FROM_MESSAGE)
        cost_product_price_in_message = cost_product_of_the_basket.text
        print(f"\ncost_product: {cost_product} ================= cost_of_basket: {cost_product_price_in_message}\n")
        assert cost_product == cost_product_price_in_message, \
        "The product cost of the basket does not match the product cost on product page"

    def element_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADDED_BASKET), \
            "Success message added basket is presented, but should not be"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADDED_BASKET), \
            "Success message \"added to basket\" should dissapeared, but it didn't"


