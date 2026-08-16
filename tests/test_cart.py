from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


class TestCart:
    def test_cart_shows_added_products(self, logged_in_page: InventoryPage, cart_page: CartPage):
        logged_in_page.add_product_to_cart("Sauce Labs Backpack")
        logged_in_page.add_product_to_cart("Sauce Labs Bike Light")
        logged_in_page.go_to_cart()

        item_names = cart_page.get_item_names()
        assert "Sauce Labs Backpack" in item_names
        assert "Sauce Labs Bike Light" in item_names
        assert cart_page.get_item_count() == 2

    def test_remove_item_from_cart_page(self, logged_in_page: InventoryPage, cart_page: CartPage):
        logged_in_page.add_product_to_cart("Sauce Labs Backpack")
        logged_in_page.go_to_cart()

        cart_page.remove_item("Sauce Labs Backpack")

        assert cart_page.get_item_count() == 0