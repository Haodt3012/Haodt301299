import pytest

@pytest.mark.usefixtures("logged_in_class")
class TestEmployeeFlow:

    def test_open_dashboard(self):
        self.page.goto("https://hrm.anhtester.com/erp/dashboard")
        self.login_page._take_screenshot("dashboard_opened")

    def test_open_employee_list(self):
        self.page.goto("https://hrm.anhtester.com/erp/employees")
        self.login_page._take_screenshot("employee_list")