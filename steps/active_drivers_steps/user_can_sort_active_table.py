from behave import *
from config import Url
from pages.login_page import LoginPage
import time
import random, string
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from pages.base import Page
from pages.active_drivers_page import ActiveDriverPage

@when('user clicks the active ID button')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.click_active_id()
    pass

@then('user can see active ID-sorted table data')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.wait_time()
    pass

@when('user clicks the active fleet number button')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.click_active_fleet_nnumber()
    pass

@then('user can see active fleet-number-sorted table data')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.wait_time()
    pass

@when('user clicks the active status button')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.click_active_status()
    pass

@then('user can see active status-sorted table data')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.wait_time()
    pass

@when('user clicks the active name button')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.click_active_name()
    pass

@then('user can see active name-sorted table data')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.wait_time()
    pass

@when('user clicks the active email button')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.click_active_email()
    pass


@then('user can see active email-sorted table data')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.wait_time()
    pass

@when('user clicks the active phone button')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.click_active_phone()
    pass

@then('user can see active phone-sorted table data')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.wait_time()
    pass

@when('user clicks the active vehicle ID button')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.click_active_vehicle_id()
    pass

@then('user can see active vechicle ID-sorted table data')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.wait_time()
    pass

@when('user clicks the active base button')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.click_active_base()
    pass

@then('user can see active base-sorted table data')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.wait_time()
    pass

@when('user clicks the active duty status button')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.click_active_duty_status()
    pass

@then('user can see active duty-status-sorted table data')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.wait_time()
    pass

@when('user clicks the active created date button')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.click_active_created_date()
    pass

@then('user can see active created-date-sorted table data')
def step_impl(context):
    page = ActiveDriverPage(context)
    page.wait_time()
    pass