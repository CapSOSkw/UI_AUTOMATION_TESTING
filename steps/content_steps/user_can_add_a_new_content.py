from behave import *
from config import Url
from pages.login_page import LoginPage
import time
import random, string
from pages.content_page import ContentPage


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

@when('user clicks the add a new content button')
def step_impl(context):
    page = ContentPage(context)
    page.click_add_a_new_content()
    pass

@then('user can add a new content')
def step_impl(context):
    page = ContentPage(context)
    page.verify_edit_elements_exist()
    pass

@then('user edits the content base')
def step_impl(context):
    page = ContentPage(context)
    page.enter_base()
    pass

@then('user edits the content title')
def step_impl(context):
    page = ContentPage(context)
    page.enter_title('Test'+randomword(2))
    pass

@then('user edits the content description')
def step_impl(context):
    page = ContentPage(context)
    page.enter_description('Test'+randomword(10))
    pass

@then('user edits the content page title')
def step_impl(context):
    page = ContentPage(context)
    page.enter_page_title('Test'+randomword(2))
    pass

@then('user edits the content page keywords')
def step_impl(context):
    page = ContentPage(context)
    page.enter_page_keywords('Test')
    pass

@then('user edits the content active status')
def step_impl(context):
    page = ContentPage(context)
    page.click_status_active()
    pass

@then('user clicks the content submit button')
def step_impl(context):
    page = ContentPage(context)
    page.click_content_submit_button()
    pass

@then('a new content is added')
def step_impl(context):
    page = ContentPage(context)
    page.wait_time()
    pass