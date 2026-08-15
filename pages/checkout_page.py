from playwright.sync_api import Page

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Etapa 1 - informações
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.error_message = page.locator("[data-test='error']")

        # Etapa 2 - revisão
        self.finish_button = page.locator("#finish")
        self.total_label = page.locator(".summary_total_label")

        # Confirmação
        self.complete_header = page.locator(".complete-header")

    def fill_information(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()

    def get_error_message(self) -> str:
        return self.error_message.text_content()

    def get_total(self) -> str:
        return self.total_label.text_content()

    def finish_order(self) -> None:
        self.finish_button.click()

    def get_confirmation_message(self) -> str:
        return self.complete_header.text_content()