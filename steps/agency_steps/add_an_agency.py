from behave import *
from pages.agency_page import AgencyPage
import random
import config
import time
@Then('user clicks add a new agency tab in the agency info page')
def step_impl(context):
    page = AgencyPage(context)
    page.click_add_an_agency()
@then('user enter an agency type in the agency info page')
def step_impl(context):
    page = AgencyPage(context)
    page.select_agency_type()
@then('user enter an agency name in the agency info page')
def step_impl(context):
    page = AgencyPage(context)
    name = "ATest" + str(random.randrange(0, 12))
    page.enter_agency_name(name)
    config.test_data["AGENCY_PAGE"][0]["NAME"] = name
@then ('user enter an agency code in the agency info page')
def step_impl(context):
    page = AgencyPage(context)
    code = str(random.randrange(0,12))
    page.enter_agency_code(code)

@then('user check days in week in the agency info page')
def step_impl(context):
    page = AgencyPage(context)
    page.select_days_in_week()
@then('user enter worktime start in the agency info page')
def step_impl(context):
    page = AgencyPage(context)
    start_hour = random.randrange(0, 12)
    config.test_data["AGENCY_PAGE"][0]["STARTHOUR"] = start_hour
    page.choose_worktime_start(start_hour)
@then('user enter worktime end in the agency info page')
def step_impl(context):
    page = AgencyPage(context)
    page = AgencyPage(context)
    end_hour = random.randrange(12, 23)
    config.test_data["AGENCY_PAGE"][0]["ENDHOUR"] = end_hour
    page.choose_worktime_end(end_hour)
@then('user enter phone in the agency info page')
def step_impl(context):
    page = AgencyPage(context)
    phone = random.randrange(3000000000,3333333333)
    config.test_data["AGENCY_PAGE"][0]["PHONE"] =phone
    page.enter_phone_number(phone)
@then('user enter email in the agency info page')
def step_impl(context):
    page = AgencyPage(context)
    email = "test" +str(random.randrange(100,3000)) +"@operr.com"
    config.test_data["AGENCY_PAGE"][0]["EMAIL"] = email
    page.enter_email(email)
@then('user enter address in the agency info page')
def step_impl(context):
    page = AgencyPage(context)
    address= "test" + str(random.randrange(100, 3000)) + "Main St Flushing"
    config.test_data["AGENCY_PAGE"][0]["EMAIL"] = address
    page.edit_agency_info(address)
@then('user enter state in the agency info page')
def step_impl(context):
    page = AgencyPage(context)
    page.select_state()
@then('user enter city in the agency info page')
def step_impl(context):
    page = AgencyPage(context)
    city = random.choice(["Queens","Brooklyn","Manhattan","Bronx"])
    page.enter_city(city)
@then('user enter zip code in the agency info page')
def step_impl(context):
    page = AgencyPage(context)
    zipcode = random.randrange(10000,11999)
    config.test_data["AGENCY_PAGE"][0]["ZIPCODE"] = zipcode
    page.enter_zipcode(zipcode)
@then('user choose active status in the agency info page')
def step_impl(context):
    page = AgencyPage(context)
    page.select_active_status()
@then('user can see the added agency in the agency page')
def step_impl(context):
    page = AgencyPage(context)
    page.choose_search_column(agency_name=config.test_data["AGENCY_PAGE"][0]["NAME"])

