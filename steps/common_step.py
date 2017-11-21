from behave import *
from selenium import webdriver
import config
from pages.login_page import LoginPage

@given('a user is logged in')
def step_impl(context):
	page = LoginPage(context)
	page.check_if_user_is_logged_in()
	pass



	# page.open("http://69.18.194.208/#/admin_login")
	# page.enter_valid_username("admin")
	# page.enter_valid_password("123456")
	# page.click_login()
	# pass