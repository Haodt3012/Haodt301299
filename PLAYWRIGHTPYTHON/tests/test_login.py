from playwright.async_api import expect
from pages.login_page import LoginPage

def test_login_successfully(page):
    login_page=LoginPage(page)
    login_page.login_withUssernamePw("admin_example","123456")