from behave import given, when, then


@given('Open sign in page')
def open_sign_in_page(context):
    context.app.sign_in_page.open_sign_in_page()


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window_handle()


@then('Log in to the page')
def log_in(context):
    context.app.sign_in_page.verify_email_input()
    context.app.sign_in_page.verify_pw_input()
    context.app.sign_in_page.input_email()
    context.app.sign_in_page.input_pw()
    context.app.sign_in_page.click_continue_btn()
