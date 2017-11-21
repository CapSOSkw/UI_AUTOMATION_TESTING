from behave import *
from config import Url
from pages.login_page import LoginPage
import time
import random, string
from pages.content_page import ContentPage

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


@when('user clicks the action edit button for the first content')
def step_impl(context):
    page = ContentPage(context)
    page.click_action_for_1st_content()
    pass

@then('user can edit a content')
def step_impl(context):
    page = ContentPage(context)
    page.verify_edit_elements_exist()
    pass

@then('user clears the content information')
def step_impl(context):
    page = ContentPage(context)
    page.clear_content_info()
    pass

@then('a content is changed')
def step_impl(context):
    page = ContentPage(context)
    page.verify_new_content_exists()
    pass