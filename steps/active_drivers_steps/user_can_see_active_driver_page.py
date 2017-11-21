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

@when('user clicks the active drivers navigation button')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.click_active_driver_tab()
    pass

@then('user can see active driver data')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.verify_active_driver_page_elements()
    pass