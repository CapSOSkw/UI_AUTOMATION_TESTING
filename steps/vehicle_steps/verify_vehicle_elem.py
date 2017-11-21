from behave import *
from pages.vehicle_page import  VehiclePage
@when ('user navigates to the vehicle page')
def step_impl(context):
    page = VehiclePage(context)
    page.visit_vehicle_page()
@then('user can see the Operr Vehicle View All Banner')
def step_impl(context):
    page = VehiclePage(context)
    page.verify_vehicle_view_all_banner()
@then('user can see show all vehicles and add a new vehicle tabs in the vehicle page')
def step_impl(context):
    page = VehiclePage(context)
    page.verify_vehicle_tabs()
@then('user can see the show entries dropdown in the vehicle page')
def step_impl(context):
    page = VehiclePage(context)
    page.verify_show_entries()
@then('user can see active lable in the vehicle page')
def step_impl(context):
    page = VehiclePage(context)
    page.verify_active_lable()
@then ('user can the result table in the vehicle page')
def step_impl(context):
    page = VehiclePage(context)
    page.verify_result_table()
@then ('user can see the searching column, searching textbox and searching bottom in the vehicle page')
def step_impl(context):
    page = VehiclePage(context)
    page.verify_search_elem()
@then ('user can see the edit button in the vehicle page')
def step_impl(context):
    page = VehiclePage(context)
    page.verify_edit_btn()