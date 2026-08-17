from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


class TestCheckout:
    def test_complete_checkout_flow(
        self,
        logged_in_page: InventoryPage,
        cart_page: CartPage,
        checkout_page: CheckoutPage,
    ):
        logged_in_page.add_product_to_cart("Sauce Labs Backpack")
        logged_in_page.go_to_cart()
        cart_page.proceed_to_checkout()

        checkout_page.fill_information("Michael", "Claudino", "12345")
        checkout_page.finish_order()

        confirmation = checkout_page.get_confirmation_message()
        assert "Thank you" in confirmation

    def test_checkout_requires_first_name(
        self,
        logged_in_page: InventoryPage,
        cart_page: CartPage,
        checkout_page: CheckoutPage,
    ):
        logged_in_page.add_product_to_cart("Sauce Labs Backpack")
        logged_in_page.go_to_cart()
        cart_page.proceed_to_checkout()

        checkout_page.fill_information("", "Claudino", "12345")

        error = checkout_page.get_error_message()
        assert "First Name is required" in error