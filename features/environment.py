import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from app.application import Application


def before_all(context):
    context.config.setup_logging()
    load_dotenv()  # Load environment variables from .env

    # Check for CLI argument first
    browser = context.config.userdata.get("browser", None)
    if browser:
        os.environ["BROWSER"] = browser  # Set it as an environment variable

    # If no CLI argument, fallback to .env or default to "chrome"
    else:
        browser = os.getenv("BROWSER", "chrome").lower()
        os.environ["BROWSER"] = browser  # Ensure it's set as env variable for later use


def browser_init(context, scenario_name):
    # Get the browser type from the environment variable or use 'chrome' as default
    browser = os.getenv("BROWSER", "chrome").lower()

    # Initialize the appropriate browser based on the selected type
    if browser == "chrome":
        driver_path = ChromeDriverManager().install()
        service = Service(driver_path)
        context.driver = webdriver.Chrome(service=service)

    elif browser == "firefox":
        driver_path = GeckoDriverManager().install()
        service = Service(driver_path)
        context.driver = webdriver.Firefox(service=service)

    elif browser == "headless":
        options = Options()
        options.add_argument("headless")
        service = Service(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(options=options, service=service)

    elif browser == "browserstack":
        bs_user = os.getenv("BS_USERNAME")
        bs_key = os.getenv("BS_KEY")
        url = f"http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub"
        options = Options()
        bstack_options = {
            "os": "Windows",
            "osVersion": "11",
            "browserName": "chrome",
            "sessionName": scenario_name,
        }
        options.set_capability("bstack:options", bstack_options)
        context.driver = webdriver.Remote(command_executor=url, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
