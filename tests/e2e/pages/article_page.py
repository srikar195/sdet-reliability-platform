class ArticlePage:
    def __init__(self, page):
        self.page = page
        self.comment_input = page.get_by_role("textbox", name="Write a comment...")
        self.post_comment_button = page.get_by_role("button", name="Post Comment")

    def add_comment(self, text: str):
        self.comment_input.fill(text)
        self.post_comment_button.click()
