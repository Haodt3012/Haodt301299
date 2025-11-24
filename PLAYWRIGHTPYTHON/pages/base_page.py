from playwright.sync_api import Page, expect, Locator, TimeoutError

class BasePage:
    """Lớp cha chứa các hành động Playwright cơ bản, kế thừa cho mọi Page Object."""

    def __init__(self, page: Page):
        self.page = page

    def _visit(self, url: str):
        """Điều hướng tới URL được chỉ định."""
        print(f"[BasePage] Truy cập: {url}")
        self.page.goto(url, wait_until="domcontentloaded")

    def _get_locator(self, locator: str) -> Locator:
        """Trả về đối tượng Locator từ chuỗi selector."""
        return self.page.locator(locator)

    def _click(self, locator: str):
        """Thực hiện click với xử lý lỗi và ghi log."""
        try:
            print(f"[Click] {locator}")
            self._get_locator(locator).click()
        except TimeoutError:
            print(f"[Lỗi] Không thể click vào {locator}")
            raise

    def _fill(self, locator: str, text: str):
        """Điền dữ liệu vào ô input."""
        print(f"[Fill] '{text}' vào {locator}")
        self._get_locator(locator).fill(text)

    def _assert_text_visible(self, locator: str, text: str):
        """Kiểm tra văn bản mong đợi hiển thị trên giao diện."""
        print(f"[Assert] Kiểm tra '{text}' hiển thị")
        expect(self._get_locator(locator)).to_contain_text(text)

    def _select_menu(self,text:str):
        locator="//li//a//span[normalize-space()={text}]"
        self._click(locator)

    def _take_screenshot(self, filename: str):
        """Lưu ảnh chụp màn hình (sử dụng khi test fail)."""
        path = f"screenshots/{filename}"
        self.page.screenshot(path=path)
        print(f"[SCREENSHOT] Lưu tại: {path}")   
