from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

# def test_login_flow():
#     with sync_playwright() as p:
#         browser=p.chromium.launch(headless=False)
#         page=browser.new_page()
#         login=LoginPage(page)

#         #1. Open website
#         login.open()
#         #2. Login
#         login.login_valid_user()
#         #3.Click locators
#         login.run_header_flow()
#         login.run_menu()
#         #4. Logout
#         login.logout()
#         browser.close()

def test_login_flow(login_page):
    login_page.open()
    login_page.login_valid_user()
    # login_page.run_header_flow()
    # login_page.run_menu()

def test_logout(login_page):
    login_page.open()
    login_page.login_valid_user()
    login_page.logout()
# def test_login_with_invalid_user():
#     with sync_playwright() as p:
#         browser=p.chromium.launch(headless=False)
#         page=browser.new_page()
#         login=LoginPage(page)

#         #1. Open website
#         login.open()
#         #2. Login
#         login.login_with_invalidUser()
#         browser.close()
        
