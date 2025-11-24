from pages.base_page import BasePage
from playwright.sync_api import expect

class Home(BasePage):
    Btn_Clockin=""
    Btn_Clockout=""

    def test_verify_ClockinButton_visble(self,text):
        self._select_menu("Home")
        assert text=="Display"
        