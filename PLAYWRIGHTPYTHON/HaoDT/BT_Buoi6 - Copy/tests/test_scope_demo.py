import pytest
from playwright.sync_api import sync_playwright

#====================================================
#FIXTURE 1: scope="function"
#-> Mỗi testcase chạy 1 lần mặc định
#====================================================
@pytest.fixture(scope="function")
def function_fixture():
    print("\n[SETUP] function_fixture")
    yield "function_scope"
    print("[TEARDOWN] function_fixture")

#====================================================
#FIXTURE 2: scope="class"
#-> Chạy 1 lần cho mỗi class
#====================================================
@pytest.fixture(scope="class")
def class_fixture():
    print("\n[SETUP] class_fixture")
    yield "class_scope"
    print("[TEARDOWN] class_fixture")

#===================================================
#FIXTURE 3:scope="module"
# -> Chạy 1 lần cho mỗi file (module)
@pytest.fixture(scope="module")
def module_fixture():
    print("\n[SETUP] module_fixture")
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        context=browser.new_context
        yield "module_scope"
        print("[TEARDOWN] module_fixture")
        context.close()
        browser.close()

#====================================================
#FIXTURE 4: scope="session"
#-> Chạy 1 lần duy nhất cho toàn bộ session pytest
@pytest.fixture(scope="session")
def session_fixture():
    print("\n[SETUP] session_fixture")
    yield "session_scope"
    print("[TEARDOWN] session_fixture")

#====================================================
# Test case sử dụng các fixture khác nhau
#====================================================
def test_case_one(module_fixture,function_fixture,session_fixture):
    print("\n--- Test Case ONE ---")
    page=module_fixture.new_page()
    page.goto("https://example.com")
    print("Page title: ",page.title())
    page.close()

def test_case_

