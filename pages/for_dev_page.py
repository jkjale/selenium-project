from selenium.webdriver.common.by import By
from pages.base_page import Page

class ForDevPage(Page):
    PAGE_TITLE = (By.XPATH, "//div[text()='for developers']")

    def verify_fd_page(self):
        self.wait_until_visible(self.PAGE_TITLE)
        self.verify_text('for developers', *self.PAGE_TITLE)
        self.verify_partial_url('for-developer')