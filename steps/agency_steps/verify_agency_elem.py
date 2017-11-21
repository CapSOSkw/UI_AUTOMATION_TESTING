from behave import *
from pages.agency_page import AgencyPage
import random
import config
import time
@when('user navigates to the agency page')
def step_impl(context):
    page = AgencyPage(context)
    page.visit_agency_page()
@Then('user can see operr agency view all banner in the agency page')
def step_impl(context):
    page = AgencyPage(context)
    page.verify_agency_banner()
@Then ('user can see show all agencys and add a new agency tabs in the agency page')
def step_impl(context):
    page = AgencyPage(context)
    page.verify_agency_tab()
@Then('user can see the show entries dropdown in the agency page')
def step_impl(context):
    page = AgencyPage(context)
    page.verify_show_entries()
@Then ('user can see the search text box, search button and searching column dropdown in the agency page')
def step_impl(context):
    page = AgencyPage(context)
    page.verify_search_column()
@Then('user can see the edit button in the agency page')
def step_impl(context):
    page = AgencyPage(context)
    page.verify_edit_btn()
