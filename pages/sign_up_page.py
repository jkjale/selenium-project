import time
from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignUpPage(Page):
    NAME_INPUT = (By.ID, "Full-Name")
    PHONE_INPUT = (By.ID, "phone2")
    EMAIL_INPUT = (By.ID, "Email-3")
    PW_INPUT = (By.ID, "field")
    CO_WEBSITE_INPUT = (By.ID, "Company-website")
    REPRESENT_DROPDOWN = (By.ID, "Role")
    POSITION_DROPDOWN = (By.ID, "Position")
    COUNTRY_DROPDOWN = (By.ID, "country-select")
    CO_SIZE_DROPDOWN = (By.ID, "Agents-amount-2")
    CREATE_ACCT_BTN = (By.XPATH, "//a[text()='Create account']")

    def open_sign_up_page(self):
        self.open_url(self.sign_up_url)

    def fill_out_form(self):
        unique_email = f"j{int(time.time())}@email.com"
        self.input_text('test+jake2+careerist', *self.NAME_INPUT)
        self.input_text('+971 + test + careerist', *self.PHONE_INPUT)
        self.input_text(unique_email, *self.EMAIL_INPUT)
        self.input_text('Password1!', *self.PW_INPUT)
        self.input_text('Test', *self.CO_WEBSITE_INPUT)
        self.select_from_dropdown('Developer', *self.REPRESENT_DROPDOWN)
        self.select_from_dropdown('Seller', *self.POSITION_DROPDOWN)
        self.select_from_dropdown('United States of America', *self.COUNTRY_DROPDOWN)
        self.select_from_dropdown('I work alone', *self.CO_SIZE_DROPDOWN)

    def click_create_account_btn(self):
        self.click(*self.CREATE_ACCT_BTN)
