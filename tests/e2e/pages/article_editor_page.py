import re


class ArticleEditorPage:
    def __init__(self, page):
        self.page = page
        self.title_input = page.get_by_role("textbox", name="Article Title")
        self.description_input = page.get_by_role("textbox", name="What's this article about?")
        self.body_input = page.get_by_role("textbox", name=re.compile("Write your article"))
        self.tags_input = page.get_by_role("textbox", name="Enter tags")
        self.publish_button = page.get_by_role("button", name="Publish Article")

    def publish_article(self, title: str, description: str, body: str, tag: str):
        self.title_input.fill(title)
        self.description_input.fill(description)
        self.body_input.fill(body)
        self.tags_input.fill(tag)
        self.publish_button.click()
