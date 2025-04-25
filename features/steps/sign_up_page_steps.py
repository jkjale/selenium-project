from behave import given, when, then

@given('Open sign up page')
def open_sign_up_page(context):
    context.app.sign_up_page.open_sign_up_page()

@when('Fill out the form')
def fill_out_form(context):
    context.app.sign_up_page.fill_out_form()

@when('Click create account button')
def click_create_account_btn(context):
    context.app.sign_up_page.click_create_account_btn()