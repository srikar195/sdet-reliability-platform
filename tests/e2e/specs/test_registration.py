from playwright.sync_api import expect
from tests.e2e.pages.home_page import HomePage
from tests.e2e.pages.register_page import RegisterPage
import uuid


def test_new_user_can_register(page):
    home = HomePage(page)
    home.goto()
    home.go_to_sign_up()

    register = RegisterPage(page)
    # register.sign_up("sdet_test_user1", "sdet_test_user1@example.com", "TestPass123!")
    unique_id = uuid.uuid4().hex[:8]
    register.sign_up(f"sdet_test_user_{unique_id}", f"sdet_test_user_{unique_id}@example.com", "TestPass123!")
    expect(page.get_by_role("link", name=f"sdet_test_user_{unique_id}")).to_be_visible()
