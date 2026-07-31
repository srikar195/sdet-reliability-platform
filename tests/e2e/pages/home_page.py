class HomePage:
    def __init__(self, page):
        self.page = page
        self.sign_up_link = page.get_by_role("link", name="Sign up")
        self.sign_in_link = page.get_by_role("link", name="Sign in")

    def goto(self):
        self.page.goto("http://localhost:4100/")

    def go_to_sign_up(self):
        self.sign_up_link.click()

    def go_to_sign_in(self):
        self.sign_in_link.click()
