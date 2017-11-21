from behave import *
import random
from selenium import webdriver
import config
from pages.admin_group_page import AdminGroupPage
@Then('user clicks edit admin group page in the admin group page')
def step_impl(context):
    page = AdminGroupPage(context)
    page.click_edit_admin_group_btn()
@Then ('user can see the admin detail information and admin information in the admin edit page')
def step_impl(context):
    page = AdminGroupPage(context)
    page.verify_edit_admin_page()
@Then ('user edit username, email, phone, address information in the admin group page')
def step_impl(context):
    page = AdminGroupPage(context)
    random.seed()
    username = "TestGroup change" + str(random.randrange(1,100))
    email ="test" +str(random.randrange(1,100))+"@operr.com"
    phone = '123456'+str(random.randrange(1000,9999))
    address = "130-30 flishing" +str(random.randrange(1,100))
    page.edit_admin_info(username,email,phone,address)
@Then ('use change status in the admin in the admin group page')
def step_impl(context):
    page = AdminGroupPage(context)
@Then ('user click submits in the admin group page')
def step_impl(context):
    page = AdminGroupPage(context)
    page.click_submit_admin_group_edits()
@Then ('the edits should be saved in the admin group page in the admin group page')
def step_impl(context):
    page = AdminGroupPage(context)
    page.verify_edit_changes()



