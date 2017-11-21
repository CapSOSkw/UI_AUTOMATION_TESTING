from behave import *
import time
from selenium import webdriver
import config
from pages.billing_page import BillingPage

@Then ('user click the result range textbox and see the daterange dropdown in the billing page')
def step_impl(context):
    page = BillingPage(context)
    page.click_the_reportrange_textbox()

@Then ('user click today button and the result range shows the right date in the billing page')
def step_impl(context):
    page = BillingPage(context)
    page.verify_today_button()
@Then ('user click yesterday button and the result range shows the right date in the billing page')

def step_impl(context):
    page = BillingPage(context)
    page.click_the_reportrange_textbox()
    page.verify_yesterday_button()
@ Then('user click last 7 days button and the result range shows the right date in the billing page')
def step_impl(context):
    page = BillingPage(context)
    page.click_the_reportrange_textbox()
    page.verify_last7days_button()
@Then('user click last 30 days button and the result range shows the right date in the billing page')
def step_impl(context):
    page = BillingPage(context)
    page.click_the_reportrange_textbox()
    page.verify_last30days_button()
@Then('user click this month button and the result range shows the right date in the billing page')
def step_impl(context):
    page = BillingPage(context)
    page.click_the_reportrange_textbox()
    page.verify_thismonth_button()
@Then ('user click last month button and the result range shows the right date in the billing page')

def step_impl(context):
    page = BillingPage(context)
    page.click_the_reportrange_textbox()
    page.verify_lastmonth_button()
@Then ('user can cancel the calendar search in the billing page')

def step_impl(context):
    page = BillingPage(context)
    page.cancel_calendar_search()



