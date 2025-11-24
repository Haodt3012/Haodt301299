from pages.project_page import Project
from playwright.sync_api import expect

def test_seach_project(page):
    project_page= Project(page)
    project_page.test_selectMenu()
    project_page.test_seach_function("12345")
