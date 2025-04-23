from behave import given, when, then


@then('Verify "For Developers" page is opened')
def verify_fd_page(context):
    context.app.for_dev_page.verify_fd_page()


@then('User can close new window and switch back to original window')
def close_page(context):
    context.app.base_page.close()
    context.app.base_page.switch_to_window_by_id(context.original_window)
