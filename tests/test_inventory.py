from pages.inventory_page import InventoryPage


class TestInventory:
    def test_add_product_to_cart(self, logged_in_page: InventoryPage):
        logged_in_page.add_product_to_cart("Sauce Labs Backpack")

        assert logged_in_page.get_cart_count() == 1

    def test_add_multiple_products_to_cart(self, logged_in_page: InventoryPage):
        logged_in_page.add_product_to_cart("Sauce Labs Backpack")
        logged_in_page.add_product_to_cart("Sauce Labs Bike Light")

        assert logged_in_page.get_cart_count() == 2

    def test_remove_product_from_cart(self, logged_in_page: InventoryPage):
        logged_in_page.add_product_to_cart("Sauce Labs Backpack")
        logged_in_page.remove_product_from_cart("Sauce Labs Backpack")

        assert logged_in_page.get_cart_count() == 0

    def test_sort_products_by_price_low_to_high(self, logged_in_page: InventoryPage):
        logged_in_page.sort_by("lohi")

        prices = logged_in_page.page.locator(".inventory_item_price").all_text_contents()
        numeric_prices = [float(p.replace("$", "")) for p in prices]

        assert numeric_prices == sorted(numeric_prices)