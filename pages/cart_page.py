from playwright.sync_api import Page

from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.checkout_button = page.locator("#checkout")
        self.cart_items = page.locator(".cart_item")
        self.continue_shopping_button = page.locator("#continue-shopping")

    def get_item_count(self) -> int:
        return self.cart_items.count()

    def get_item_names(self) -> list[str]:
        return self.page.locator(".inventory_item_name").all_text_contents()

    def proceed_to_checkout(self) -> None:
        self.checkout_button.click()

    def remove_item(self, product_name: str) -> None:
        item = self.page.locator(".cart_item", has_text=product_name)
        item.locator("button", has_text="Remove").click()