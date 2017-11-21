from behave import *
from config import Url
from pages.login_page import LoginPage
import time
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from pages.base import Page

@when('user is on the admin page')
def step_impl(context):
    page = AdminPage(context)
    page.click_admin_tab()
    pass

@when('user clicks the status button')
def step_impl(context):
    page = AdminPage(context)
    page.click_table_status()
    pass

@then('user can see status-sorted table data')
def step_impl(context):
    page = AdminPage(context)
    page.wait_time()
    pass

@when('user clicks the username button')
def step_impl(context):
    page = AdminPage(context)
    page.click_table_username()
    pass

@then('user can see username-sorted table data')
def step_impl(context):
    page = AdminPage(context)
    page.wait_time()
    pass

@when('user clicks the email button')
def step_impl(context):
    page = AdminPage(context)
    page.click_table_email()
    pass

@then('user can see email-sorted table data')
def step_impl(context):
    page = AdminPage(context)
    page.wait_time()
    pass

@when('user clicks the phone button')
def step_impl(context):
    page = AdminPage(context)
    page.click_table_email()
    pass

@then('user can see phone-sorted table data')
def step_impl(context):
    page = AdminPage(context)
    page.wait_time()
    pass

@when('user clicks the 2nd phone button')
def step_impl(context):
    page = AdminPage(context)
    page.click_table_2ndphone()
    pass

@then('user can see 2nd-phone-sorted table data')
def step_impl(context):
    page = AdminPage(context)
    page.wait_time()
    pass

@when('user clicks the admin level button')
def step_impl(context):
    page = AdminPage(context)
    page.click_table_admin_lvl()
    pass

@then('user can see admin-level-sorted table data')
def step_impl(context):
    page = AdminPage(context)
    page.wait_time()
    pass

@when('user clicks the company button')
def step_impl(context):
    page = AdminPage(context)
    page.click_table_company()
    pass

@then('user can see company-sorted table data')
def step_impl(context):
    page = AdminPage(context)
    page.wait_time()
    pass

@when('user clicks the base button')
def step_impl(context):
    page = AdminPage(context)
    page.click_table_base()
    pass

@then('user can see base-sorted table data')
def step_impl(context):
    page = AdminPage(context)
    page.wait_time()
    pass

@when('user clicks the name button')
def step_impl(context):
    page = AdminPage(context)
    page.click_table_name()
    pass

@then('user can see name-sorted table data')
def step_impl(context):
    page = AdminPage(context)
    page.wait_time()
    pass