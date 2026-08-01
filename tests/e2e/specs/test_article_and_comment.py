import uuid
from playwright.sync_api import expect
from tests.e2e.pages.home_page import HomePage
from tests.e2e.pages.register_page import RegisterPage
from tests.e2e.pages.article_editor_page import ArticleEditorPage
from tests.e2e.pages.article_page import ArticlePage


def test_user_can_publish_article_and_comment(page):
    unique_id = uuid.uuid4().hex[:8]
    username = f"sdet_test_user_{unique_id}"
    email = f"{username}@example.com"
    password = "TestPass123!"
    article_title = f"SDET Test Article {unique_id}"

    home = HomePage(page)
    home.goto()
    home.go_to_sign_up()

    register = RegisterPage(page)
    register.sign_up(username, email, password)
    expect(page.get_by_role("link", name=username)).to_be_visible()

    home.go_to_new_post()
    editor = ArticleEditorPage(page)
    editor.publish_article(
        title=article_title,
        description="A test article created by automated E2E test",
        body="This article exists purely to validate the publish flow.",
        tag="sdet-test",
    )
    expect(page.get_by_role("heading", name=article_title)).to_be_visible()

    article = ArticlePage(page)
    article.add_comment("Great read, thanks for sharing!")
    expect(page.get_by_text("Great read, thanks for sharing!")).to_be_visible()
