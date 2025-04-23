from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    email = '***'
    pw = '***'
    EMAIL_INPUT = (By.ID, "email-2")
    PW_INPUT = (By.ID, "field")
    CONTINUE_BTN = (By.XPATH, "//a[text()='Continue']")

    def open_sign_in_page(self):
        self.open_url(self.sign_in_url)

    def verify_email_input(self):
        self.wait_until_clickable(self.EMAIL_INPUT)

    def verify_pw_input(self):
        self.wait_until_clickable(self.PW_INPUT)

    def input_email(self):
        self.input_text(self.email, *self.EMAIL_INPUT)

    def input_pw(self):
        self.input_text(self.pw, *self.PW_INPUT)

    def click_continue_btn(self):
        self.wait_until_clickable_click(self.CONTINUE_BTN)