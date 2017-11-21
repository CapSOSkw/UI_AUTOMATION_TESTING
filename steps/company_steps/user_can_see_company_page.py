from behave import *
from config import Url
from pages.login_page import LoginPage
import time
import random, string
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from pages.base import Page
from pages.inactive_drivers_page import InactiveDriverPage
from pages.company_page import CompanyPage

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

@when('user clicks the company navigation button')
def step_impl(context):
    page = CompanyPage(context)
    page.click_company_navigation_tab()
    pass

@then('user can see all companies data')
def step_impl(context):
    page = CompanyPage(context)
    page.verify_company_elements_exist()
    pass
