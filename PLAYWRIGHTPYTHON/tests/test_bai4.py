from playwright.sync_api import sync_playwright,expect
import time
def test_run():
    with sync_playwright() as p:
        browser= p.chromium.launch(headless=False,channel="chrome")
        context=browser.new_context()
        page=context.new_page()
        #dropdown
        
        # page.goto("https://www.saucedemo.com")
        # page.locator("#user-name").fill("standard_user")
        # page.locator("#password").fill("secret-sauce")
        # page.goto("https://the-internet.herokuapp.com/dropdown")
        # page.locator("#dropdown").select_option("2")
        # time.sleep(5)
        
        #click
        
        # page.goto("https://cms.anhtester.com/login")
        # page.locator("#email").fill("abcd@gmail.com")
        # page.locator("#password").fill("123456")
        # page.locator("//span[@class='aiz-square-check']").click()
        
        #upload
        
        # page.goto("https://the-internet.herokuapp.com/upload")
        # #page.locator("#file-upload").set_input_files("300.png")
        # page.set_input_files("input[type='file']",["data/300.png"])
        # page.get_by_role("button",name="upload").click()
        
        #hover
        try:
            page.goto("https://letcode.in/")
        #page.locator("//div[contains(@class,'dropdown')]//a[normalize-space()='Grooming']").hover()
            dropdown=page.locator("//div[contains(@class,'dropdown')]//a[normalize-space()='Grooming']").hover()
            expect(dropdown).to_be_visible()#truyển timeout= ... để chỉ check trong bao nhiêu mili s
        finally:
            page.get_attribute("//a[@id='link']",'value')
            time.sleep(5)
        #get text
        
        
        #page.locator(".username").text_content()
        #page.text_content("//textbox[@id='username]")
        time.sleep(10)
        context.close()
        browser.close()
if __name__=="__main__":
    test_run()
        