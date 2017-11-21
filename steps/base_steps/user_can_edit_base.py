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

@when('user clicks action button for the first base')
def step_impl(context):
    page = BasePage(context)
    page.click_action_button_for_1st_base()
    pass

@then('user can edit the base')
def step_impl(context):
    page = BasePage(context)
    page.verify_edit_base_page_elements()
    pass

@then('user clear the base data')
def step_impl(context):
    page = BasePage(context)
    page.clear_base_data()
    pass