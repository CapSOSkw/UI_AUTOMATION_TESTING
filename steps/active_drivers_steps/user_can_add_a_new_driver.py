from behave import *
from config import Url
from pages.login_page import LoginPage
import time
import random, string
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from pages.base import Page
from pages.inactive_drivers_page import InactiveDriverPage
from pages.active_drivers_page import ActiveDriverPage

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

@when('user clicks add a new driver button')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.click_add_a_new_driver()
    page.wait_time()
    pass

@then('user can add a new driver')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.verify_information_exists()
    pass

@then('user edits the active driver dsp percent')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_dsp_percent('10')
    pass

@then('user edits the active driver base percent')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_base_percent('20')
    pass

@then('user edits the active driver driver percent')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_driver_percent('30')
    pass

@then('user edits the active driver reserve percent')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.enter_reserve_percent('40')
    pass

@then('user clicks the active driver base approved active')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.click_base_approved_active()
    pass