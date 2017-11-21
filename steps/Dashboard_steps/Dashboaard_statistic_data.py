from behave import *
from config import Url
from pages.login_page import LoginPage
import time
from pages.dashboard_page import DashboardPage
from pages.base import Page

@when('user navigates to statistic page')
def step_impl(context):
    page = DashboardPage(context)
    page.click_statistic_btn()
    pass

@then('user can see statistic data')
def step_impl(context):
    page = DashboardPage(context)
    page.verify_statistic_elements_exist()
    pass

@when('user clicks auto refresh button')
def step_impl(context):
    page = DashboardPage(context)
    page.click_atuo_refresh()
    pass

@then('webpage keeps refreshing')
def step_impl(context):
    page = DashboardPage(context)
    page.wait_time()
    page.wait_time()
    pass

@when('user clicks stop auto refresh button')
def step_impl(context):
    page = DashboardPage(context)
    page.click_stop_refresh()
    pass

@then('webpage stops refreshing')
def step_impl(context):
    page = DashboardPage(context)
    page.wait_time()
    pass

@when('user clicks manual refresh button')
def step_impl(context):
    page = DashboardPage(context)
    page.click_manual_refresh()
    pass

@then('webpage refreshes once')
def step_impl(context):
    page = DashboardPage(context)
    page.wait_time()
    pass

@when('user clicks heat map')
def step_impl(context):
    page = DashboardPage(context)
    page.click_heat_map()
    pass

@then('user can see heat map')
def step_impl(context):
    page = DashboardPage(context)
    page.wait_time()
    pass

@when('user clicks trips button')
def step_impl(context):
    page = DashboardPage(context)
    page.click_trips()
    pass

@then('user navigates to trip history page')
def step_impl(context):
    page = DashboardPage(context)
    page.navigate_to_trip_history()
    page.wait_time()
    pass

@when('user clicks driver on off duty')
def step_impl(context):
    page = DashboardPage(context)
    page.click_driver_on_off_duty()
    pass

@then('user navigates to driver on off duty')
def step_impl(context):
    page = DashboardPage(context)
    page.navigate_to_drive_duty()
    page.wait_time()
    pass