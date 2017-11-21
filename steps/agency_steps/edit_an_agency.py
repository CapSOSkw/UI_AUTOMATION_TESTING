from behave import *
from pages.agency_page import AgencyPage
import random
import config
import time

@Then('user sort the table by ID and click the edit button in the agency page')
def step_impl(context):
    page = AgencyPage(context)
    page.sort_by_ID()
    page.click_edit_btn()
@then('user edits the infomation in the agency info page')
def step_impl(context):
    page = AgencyPage(context)
    address = str(random.randrange(1000,9999))+"Flushing"
    config.test_data['AGENCY_PAGE'][0]['ADDRESS'] = address
    page.edit_agency_info(address)
@then('user clicks submit button in the agency info page')
def step_impl(context):
    page = AgencyPage(context)
    page.click_submit()
    time.sleep(5)
@then ('user can see the edits in the agency page')
def step_impl(context):
    page = AgencyPage(context)



