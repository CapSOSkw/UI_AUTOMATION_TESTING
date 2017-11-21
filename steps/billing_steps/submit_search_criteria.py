from behave import *
import time
from selenium import webdriver
import config
from pages.billing_page import BillingPage

@Then ('user can choose company info dropdown in the billing page')
def step_impl(context):
    page = BillingPage(context)
    page.select_companyinfo_dropdown()

@Then ('user can choose base info dropdown in the billing page')
def step_impl(context):
    page = BillingPage(context)
    page.select_baseinfo_dropdown()
@Then ('user can choose agency name dropdown in the billing page')
def step_impl(context):
    page = BillingPage(context)
    page.select_agencyname_dropdown()
@Then ('user can choose driver info dropdown in the billing page')
def step_impl(context):
    page = BillingPage(context)
    page.select_driverinfo_dropdown()
@Then ('user can submit search criteria and see the result table in the billing page')
def step_impl(context):
    page=BillingPage(context)
    page.submit_search_critira()

