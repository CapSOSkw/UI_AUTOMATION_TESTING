from behave import *
from pages.admin_group_page import AdminGroupPage
@when ('user navigates to the admin group page')
def step_impl(context):
    page = AdminGroupPage(context)
    page.visit_admin_group_page()
@Then ('user can see the show_all_admin_group and add_a_new_group tabs in the admin group page')
def step_impl(context):
    page = AdminGroupPage(context)
    page.verify_show_all_admin_group_tab()
    page.verify_add_a_new_group_tab()

@Then ('user can see the show entries dropdown and text in the admin group page')
def step_impl(context):
    page = AdminGroupPage(context)
    page.verify_show_entries_dropdown()
@Then ('user can see the action buttons in the admin group page')
def step_impl(context):
    page = AdminGroupPage(context)
    page.verify_edit_admin_group_btn()
