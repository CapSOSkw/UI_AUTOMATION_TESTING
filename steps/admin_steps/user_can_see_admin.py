from behave import *
from config import Url
from pages.login_page import LoginPage
import time
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from pages.base import Page

@when('user clicks the admin navigation button')
def step_impl(context):
    page = AdminPage(context)
    page.click_admin_tab()
    pass

@then('user can see the all admin data')
def step_impl(context):
    page = AdminPage(context)
    page.verify_admin_page_elements()
    pass
