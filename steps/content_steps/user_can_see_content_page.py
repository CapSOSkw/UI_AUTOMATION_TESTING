from behave import *
from config import Url
from pages.login_page import LoginPage
import time
import random, string
from pages.content_page import ContentPage


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

@when('user clicks the content navigation button')
def step_impl(context):
    page = ContentPage(context)
    page.click_content_navigation_tab()
    pass

@then('user can see all content data')
def step_impl(context):
    page = ContentPage(context)
    page.verify_content_elements_exist()
    pass