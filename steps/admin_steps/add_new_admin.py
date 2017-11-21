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

@when('user clicks add a new admin button')
def step_impl(context):
    page = AdminPage(context)
    page.click_add_new_admin_btn()
    pass

@then('user can add a new admin')
def step_impl(context):
    page = AdminPage(context)
    page.wait_time()
    pass

@then('user enters first name')
def step_impl(context):
    page = AdminPage(context)
    page.enter_firstname('A'+randomword(2))
    pass

@then('user enters last name')
def step_impl(context):
    page = AdminPage(context)
    page.enter_lastname('A'+randomword(2))
    pass

@then('user enters username')
def step_impl(context):
    page = AdminPage(context)
    page.enter_username('A'+randomword(3))
    pass

@then('user enters email address')
def step_impl(context):
    page = AdminPage(context)
    page.enter_email_address('A'+randomword(2))
    pass

@then('user creates password')
def step_impl(context):
    page = AdminPage(context)
    page.enter_password('123456')
    pass

@then('user enters valid phone number')
def step_impl(context):
    page = AdminPage(context)
    page.enter_add_phone('1234567890')
    pass

@then('user chooses a permission level')
def step_impl(context):
    page = AdminPage(context)
    page.choose_permission_lvl_ADD()
    pass

@then('user chooses a company')
def step_impl(context):
    page = AdminPage(context)
    page.choose_company_ADD()
    pass

@then('user chooses a base')
def step_impl(context):
    page = AdminPage(context)
    page.choose_base_ADD()
    pass

@then('user clicks active button')
def step_impl(context):
    page = AdminPage(context)
    page.click_active()
    pass

@then('user submits')
def step_impl(context):
    page = AdminPage(context)
    page.click_submit_btn()
    page.wait_time()
    pass

@then('a new admin is added')
def step_impl(context):
    page = AdminPage(context)
    page.click_table_username()
    page.wait_time()
    page.verify_new_username_exist()
    pass
