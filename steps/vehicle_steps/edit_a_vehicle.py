from behave import *
import random
from pages.vehicle_page import  VehiclePage
import config
@then ('user sort users by VIN and clicks edit button in the vehicle page')
def step_impl(context):
    page = VehiclePage(context)
    page.click_sort_vin_btn()
    page.click_edit_btn()
@then ('user edit vehicle information in the vehicle information page')
def step_impl(context):
    page = VehiclePage(context)
    platenumber = "A" + str(random.randrange(100000, 999999))
    config.test_data['VEHICLE_PAGE'][0]['PLATENUMBER']=platenumber
    liability = str(random.randrange(10000, 99999))
    config.test_data['VEHICLE_PAGE'][0]['LIABILITY']= liability
    page.edit_vehicle_information(platenumber,liability)
@then('user clicks submit in the vehicle information page')
def step_impl(context):
    page = VehiclePage(context)
    page.click_submit_btn()
@then('user can user search textbox and find the edits in the vehicle page')
def step_impl(context):
    page = VehiclePage(context)
    page.click_search_column()





########Click doesn't work
