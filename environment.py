
from selenium import webdriver

def before_all (context):
	
	path = './chromedriver'

	# define Chrome browser instances
	context.browser = webdriver.Chrome(path)
	context.browser.maximize_window()

def after_all(context):
	# close browsers after all have been executed
	context.browser.quit()

	