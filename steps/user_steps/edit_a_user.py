from behave import *
import random
from pages.user_page import UserPage
@then('user sort users by username and clicks edit button in the user page')
def step_impl(context):
    page = UserPage(context)
    page.click_edit_button()
@then('user edit username, email, firstname, lastname,phone and address information in the user information page')
def step_impl(context):
    page = UserPage(context)
    random.seed()
    username = "123" + str(random.randrange(1, 10))
    firstname = "YU" + str(random.randrange(1,9))
    lastname = "Fang" +str(random.randrange(1,9))
    email = "test" + str(random.randrange(1, 100)) + "@operr.com"
    phone = '123456' + str(random.randrange(1000, 9999))
    address = "130-30 flishing" + str(random.randrange(1, 100))
    page.edit_user_information(username, email,firstname,lastname,phone, address)
@then('user clicks submit in the user information page')
def step_impl(context):
    page = UserPage(context)
@then('user can see changed user information')
def step_impl(context):
    page = UserPage(context)

