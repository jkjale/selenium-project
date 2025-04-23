from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):
    CTD_BTN = (By.XPATH, "//div[text()='Connect the developer']")

    def click_ctd_btn(self):
        self.wait_until_clickable_click(self.CTD_BTN)
