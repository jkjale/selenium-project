from behave import given, when, then

@when('Click on "Connect the developer" button')
def click_connect_the_developer_btn(context):
    context.app.main_page.click_ctd_btn()

@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.base_page.switch_to_new_window()