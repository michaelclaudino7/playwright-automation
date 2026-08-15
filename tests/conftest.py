import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def inventory_page(page: Page) -> InventoryPage:
    return InventoryPage(page)


@pytest.fixture
def cart_page(page: Page) -> CartPage:
    return CartPage(page)


@pytest.fixture
def checkout_page(page: Page) -> CheckoutPage:
    return CheckoutPage(page)


@pytest.fixture
def logged_in_page(login_page: LoginPage) -> InventoryPage:
    """Fixture que já entrega o usuário logado, pronto pra testar outras páginas."""
    from config.settings import STANDARD_USER, PASSWORD

    login_page.open()
    login_page.login(STANDARD_USER, PASSWORD)
    return InventoryPage(login_page.page)