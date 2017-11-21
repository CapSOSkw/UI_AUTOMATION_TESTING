from behave import *
from config import Url
from pages.login_page import LoginPage
import time
import random, string
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from pages.base import Page
from pages.inactive_drivers_page import InactiveDriverPage
from pages.base_page import BasePage

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

@when('user clicks the base status button')
def step_impl(context):
    page = BasePage(context)
    page.click_table_status()
    pass

@then('user can see base status-sorted table data')
def step_impl(context):
    page = BasePage(context)
    page.wait_time()
    pass

@when('user clicks the base base name button')
def step_impl(context):
    page = BasePage(context)
    page.click_table_base_name()
    pass

@then('user can see base based-name-sorted table data')
def step_impl(context):
    page = BasePage(context)
    page.wait_time()
    pass

@when('user clicks the base base type button')
def step_impl(context):
    page = BasePage(context)
    page.click_table_base_type()
    pass


@then('user can see base base-type-sorted table data')
def step_impl(context):
    page = BasePage(context)
    page.wait_time()
    pass

@when('user clicks the base company button')
def step_impl(context):
    page = BasePage(context)
    page.click_table_company()
    pass

@then('user can see base company-sorted table data')
def step_impl(context):
    page = BasePage(context)
    page.wait_time()
    pass

@when('user clicks the base fare type button')
def step_impl(context):
    page = BasePage(context)
    page.click_table_fare_type()
    pass

@then('user can see base fare-type-sorted table data')
def step_impl(context):
    page = BasePage(context)
    page.wait_time()
    pass