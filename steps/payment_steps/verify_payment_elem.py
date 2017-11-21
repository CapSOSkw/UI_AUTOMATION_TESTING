from behave import *
import time
from selenium import webdriver
import config
from pages.payment_page import PaymentPage



@when ('user navigates to the payment page')
def step_impl(context):
    page = PaymentPage(context)
    page.visit_payment_page()
@Then ('user can see companyinfo dropdown in the payment page')
def step_impl(context):
    page = PaymentPage(context)
    page.verify_companyinfo_dropdown_exists()
@Then ('user can see agencyname dropdown in the payment page')
def step_impl(context):
    page = PaymentPage(context)
    page.verify_agencyname_dropdown_exsits()
@Then ('user can see calendar in the payment page')
def step_impl(context):
    page= PaymentPage(context)
    page.verify_calendar_exists()
@Then ('user can see submit button in the payment page')
def  step_impl(context):
    page=PaymentPage(context)
    page.verify_submit_button_exists()
