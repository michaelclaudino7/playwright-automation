import pytest

from config.settings import STANDARD_USER, PASSWORD, LOCKED_OUT_USER
from pages.login_page import LoginPage


class TestLogin:
    def test_successful_login(self, login_page: LoginPage):
        login_page.open()
        login_page.login(STANDARD_USER, PASSWORD)

        assert "inventory.html" in login_page.page.url

    def test_login_with_locked_out_user(self, login_page: LoginPage):
        login_page.open()
        login_page.login(LOCKED_OUT_USER, PASSWORD)

        error = login_page.get_error_message()
        assert "locked out" in error.lower()

    def test_login_with_invalid_password(self, login_page: LoginPage):
        login_page.open()
        login_page.login(STANDARD_USER, "senha_errada")

        error = login_page.get_error_message()
        assert "do not match" in error.lower()