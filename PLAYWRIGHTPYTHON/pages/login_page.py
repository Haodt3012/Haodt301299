from .base_page import BasePage
from playwright.sync_api import expect, Playwright
import time

class LoginPage(BasePage):
    URL="https://hrm.anhtester.com/erp/login"
    Username="#iusername"
    Password="#ipassword"
    BtnLogin="//button[@type='submit']"

    
    def goto(self) :
        # browser = playwright.chromium.launch(headless=False) 
        self._visit(self.URL)
    
    def login_withUssernamePw(self,username,password):
        self.goto()
        self._fill(self.Username,username)
        self._fill(self.Password,password)
        self._click(self.BtnLogin)
        time.sleep(5)
        
    
