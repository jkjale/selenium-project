from pages.base_page import Page
from pages.for_dev_page import ForDevPage
from pages.main_page import MainPage
from pages.sign_in_page import SignInPage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)
        self.for_dev_page = ForDevPage(driver)
        self.main_page = MainPage(driver)
        self.sign_in_page = SignInPage(driver)
