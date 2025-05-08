from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):
    CTD_BTN = (By.XPATH, "//div[text()='Connect the developer']")
    SETTINGS_GEAR_ICON = (By.CSS_SELECTOR, ".settings-code.w-embed")
    SETTINGS_LINK = (By.XPATH, "//div[text()='Settings']")

    def click_ctd_btn(self):
        self.wait_until_clickable_click(self.CTD_BTN)

    def verify_settings_link(self):
        self.wait_until_visible(self.SETTINGS_LINK)

    def verify_settings_link_mobile(self):
        self.wait_until_visible(self.SETTINGS_GEAR_ICON)