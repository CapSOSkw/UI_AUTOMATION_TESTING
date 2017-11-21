from behave import *
import random
from pages.admin_group_page import AdminGroupPage
@When ('user navigates to the add a new group page')
def step_impl(context):
    page = AdminGroupPage(context)
    page.click_add_a_new_group_tab()
@Then ('user can enter username, email, phone, address information in the add a new group page')
def step_impl(context):
    page = AdminGroupPage(context)
    random.seed()
    username = "TestGroup change" + str(random.randrange(1, 100))
    email = "test" + str(random.randrange(1, 100)) + "@operr.com"
    phone = '123456' + str(random.randrange(1000, 9999))
    address = "120-30 flishing" + str(random.randrange(1, 100))
    page.add_a_new_group_info(username, email, phone, address)
@Then ('user can click the active pointer in the add a new group page')
def step_impl(context):
    page = AdminGroupPage(context)
    page.change_status_pointer()
@Then ('user can submit created values in the add a new group page')
def step_impl(context):
    page = AdminGroupPage(context)
    page.click_submit_admin_group_edits()
@Then ('user can see the created values in the admin group page')
def step_impl(context):
    page = AdminGroupPage(context)
    page.verify_edit_changes()