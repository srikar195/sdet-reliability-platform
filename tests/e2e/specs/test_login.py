import uuid
from playwright.sync_api import expect
from tests.e2e.pages.home_page import HomePage
from tests.e2e.pages.register_page import RegisterPage
from tests.e2e.pages.login_page import LoginPage


def test_registered_user_can_log_in(browser):
    unique_id = uuid.uuid4().hex[:8]
    username = f"sdet_test_user_{unique_id}"
    email = f"{username}@example.com"
    password = "TestPass123!"

    # Setup: create the account in its own throwaway session
    setup_context = browser.new_context()
    setup_page = setup_context.new_page()
    setup_home = HomePage(setup_page)
    setup_home.goto()
    setup_home.go_to_sign_up()
    register = RegisterPage(setup_page)
    register.sign_up(username, email, password)
    expect(setup_page.get_by_role("link", name=username)).to_be_visible()
    setup_context.close()

    # Actual test: log in as that user in a brand new, unauthenticated session
    login_context = browser.new_context()
    login_page = login_context.new_page()
    login_home = HomePage(login_page)
    login_home.goto()
    login_home.go_to_sign_in()
    login = LoginPage(login_page)
    login.login(email, password)

    expect(login_page.get_by_role("link", name=username)).to_be_visible()
    login_context.close()
