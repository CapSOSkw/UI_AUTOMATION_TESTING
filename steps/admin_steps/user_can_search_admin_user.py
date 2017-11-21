from behave import *
from config import Url
from pages.login_page import LoginPage
import time
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from pages.base import Page

@then('user types a text in the search box')
def step_impl(context):
    page = AdminPage(context)
    page.enter_text_in_search_box('Cheng')
    pass

@then('user clicks the search button in the admin page')
def step_impl(context):
    page = AdminPage(context)
    page.click_searching_btn()
    pass

@then('result containing text should display')
def step_impl(context):
    page = AdminPage(context)
    page.verify_search_result()
    page.wait_time()
    page.clear_search_box()
    page.wait_time()
    pass
