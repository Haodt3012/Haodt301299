from pages.base_page import BasePage
from playwright.sync_api import expect

class Project(BasePage):
    Btn_Clockin=""
    Btn_Clockout=""
    seach_box=""

    def test_selectMenu(self,text):
        self._select_menu("Projects")
        assert text=="Display"

        
    def test_seach_function(self,name:str):
        self._fill(self.seach_box,name)