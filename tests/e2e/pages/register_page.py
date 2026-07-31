class RegisterPage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.email_input = page.get_by_role("textbox", name="Email")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.submit_button = page.get_by_role("button", name="Sign up")

    def sign_up(self, username: str, email: str, password: str):
        self.username_input.fill(username)
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_button.click()
