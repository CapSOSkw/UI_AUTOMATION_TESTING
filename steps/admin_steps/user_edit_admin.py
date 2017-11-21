from behave import *
from config import Url
from pages.login_page import LoginPage
import time
import random, string
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from pages.base import Page

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

@when('user clicks action button for the first username')
def step_impl(context):
    page = AdminPage(context)
    page.click_action_btn()
    pass

@then('user can see all information of this admin')
def step_impl(context):
    page = AdminPage(context)
    page.verify_edit_admin_elements_exist()
    pass

@then('user clears all the information')
def step_impl(context):
    page = AdminPage(context)
    page.clear_all_information()
    pass

@then('user edits first name')
def step_impl(context):
    page = AdminPage(context)
    page.enter_firstname('A'+randomword(2))
    pass

@then('user edits last name')
def step_impl(context):
    page = AdminPage(context)
    page.enter_lastname('A'+randomword(2))
    pass

@then('user edits username')
def step_impl(context):
    page = AdminPage(context)
    page.enter_username('A'+randomword(4))
    pass

@then('user edits email address')
def step_impl(context):
    page = AdminPage(context)
    page.enter_email_address('A'+randomword(2))


@then('user edits phone number')
def step_impl(context):
    page = AdminPage(context)
    page.enter_edit_phone('1234567890')
    pass

@then('user rechooses a permission level')
def step_impl(context):
    page = AdminPage(context)
    page.choose_permission_lvl_EDIT()
    pass

@then('user rechooses a company')
def step_impl(context):
    page = AdminPage(context)
    page.choose_company_EDIT()
    pass

@then('user rechooses a base')
def step_impl(context):
    page = AdminPage(context)
    page.choose_base_EDIT()
    pass

@then('user clicks the admin active status')
def step_impl(context):
    page = AdminPage(context)
    page.click_status_active()
    pass

@then('user clicks submit button on edit page')
def step_impl(context):
    page = AdminPage(context)
    page.click_submit_button_edit_page()
    pass

@then('an admin is changed')
def step_impl(context):
    page = AdminPage(context)
    page.verify_new_username_exist()
    page.wait_time()
    pass