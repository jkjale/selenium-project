import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from app.application import Application
from support.logger import logger

# Command to run tests with Allure & Behave
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/main_page_ui.feature

# Generate Allure report
# allure serve test_results/

# Behave commands
# behave
# behave -D browser=browserstack


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
    print("Using browser:", browser)

def browser_init(context, scenario_name):
    # Get the browser type from the environment variable or use 'chrome' as default
    browser = os.getenv("BROWSER", "chrome").lower()

    # Initialize the appropriate browser based on the selected type
    if browser == "chrome":
        # Check if we need to emulate a mobile device
        device_name = os.getenv("MOBILE_EMULATION", None)
        chrome_options = Options()
        if device_name:
            # Set up mobile emulation for a specific device (e.g., Nexus 5)
            mobile_emulation = {
                "deviceName": device_name  # Fetches the device name from the env
            }
            chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        driver_path = ChromeDriverManager().install()
        service = Service(driver_path)
        context.driver = webdriver.Chrome(service=service, options=chrome_options)
        context.driver.maximize_window()

    elif browser == "firefox":
        driver_path = GeckoDriverManager().install()
        service = Service(driver_path)
        context.driver = webdriver.Firefox(service=service)
        context.driver.maximize_window()

    elif browser == "headless":
        options = Options()
        options.add_argument("headless")
        service = Service(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(options=options, service=service)

    elif browser == "browserstack":
        # Register for BrowserStack, then grab user and key from https://www.browserstack.com/accounts/settings
        # To change devices go to https://www.browserstack.com/docs/automate/capabilities and go to "Legacy" and choose device
        bs_user = os.getenv("BS_USERNAME")
        bs_key = os.getenv("BS_KEY")
        url = f"http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub"
        options = Options()
        bstack_options = {
            "osVersion" : "13.0",
            "deviceName" : "Samsung Galaxy S23 Ultra",
            "consoleLogs" : "info",
            "sessionName": scenario_name,
        }
        options.set_capability("bstack:options", bstack_options)
        context.driver = webdriver.Remote(command_executor=url, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    print(f"Selected browser: {browser}")
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.warning(f'Step failed: {step}')


def after_scenario(context, feature):
    context.driver.quit()
