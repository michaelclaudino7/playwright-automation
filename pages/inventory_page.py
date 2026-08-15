from playwright.sync_api import Page

from pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.inventory_items = page.locator(".inventory_item")
        self.sort_dropdown = page.locator(".product_sort_container")

    def add_product_to_cart(self, product_name: str) -> None:
        item = self.page.locator(".inventory_item", has_text=product_name)
        item.locator("button", has_text="Add to cart").click()

    def remove_product_from_cart(self, product_name: str) -> None:
        item = self.page.locator(".inventory_item", has_text=product_name)
        item.locator("button", has_text="Remove").click()

    def get_cart_count(self) -> int:
        if self.cart_badge.count() == 0:
            return 0
        return int(self.cart_badge.text_content())

    def go_to_cart(self) -> None:
        self.cart_link.click()

    def get_product_names(self) -> list[str]:
        return self.page.locator(".inventory_item_name").all_text_contents()

    def sort_by(self, option_value: str) -> None:
        self.sort_dropdown.select_option(option_value)