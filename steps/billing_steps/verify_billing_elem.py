from behave import *
import time
from selenium import webdriver
import config
from pages.billing_page import BillingPage



@when ('user navigates to the billing page')
def step_impl(context):
    page = BillingPage(context)
    page.visit_billing_page()
@Then ('user can see companyinfo dropdown in the billing page')
def step_impl(context):
    page = BillingPage(context)
    page.verify_companyinfo_dropdown_exists()
@Then ('user can see agencyname dropdown in the billing page')
def step_impl(context):
    page = BillingPage(context)
    page.verify_agencyname_dropdown_exsits()
@Then ('user can see calendar in the billing page')
def step_impl(context):
    page= BillingPage(context)
    page.verify_calendar_exists()
@Then ('user can see submit button in the billing page')
def  step_impl(context):
    page=BillingPage(context)
    page.verify_submit_button_exists()
