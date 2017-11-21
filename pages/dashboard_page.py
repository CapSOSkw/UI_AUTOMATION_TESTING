from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .base import Page
from locators.locators import *
import time

class DashboardPage(Page):

    def __init__(self, context):
        Page.__init__(self, context)


    def verify_elements_exist(self):
        self.find_element(*DashboardPageLocators.ANALYSIS_BTN)
        self.find_element(*DashboardPageLocators.STATISTIC_BTN)
        self.find_element(*DashboardPageLocators.MONTH_3)
        self.find_element(*DashboardPageLocators.MONTH_6)
        self.find_element(*DashboardPageLocators.MONTH_12)
        self.find_element(*DashboardPageLocators.AREA_CHART)
        self.find_element(*DashboardPageLocators.PIE_CHART)
        self.find_element(*DashboardPageLocators.PERC_COLU_CHART)

    def verify_statistic_elements_exist(self):
        self.find_element(*DashboardPageLocators.AUTO_REFRESH_BTN)
        self.find_element(*DashboardPageLocators.MANUAL_REFRESH_BTN)

    def wait_time(self):
        time.sleep(5)

    def click_month_3_btn(self):
        month_3_btn = self.find_element(*DashboardPageLocators.MONTH_3)
        month_3_btn.click()

    def click_month_6_btn(self):
        month_6_btn = self.find_element(*DashboardPageLocators.MONTH_6)
        month_6_btn.click()

    def click_month_12_btn(self):
        month_12_btn = self.find_element(*DashboardPageLocators.MONTH_12)
        month_12_btn.click()

    def click_statistic_btn(self):
        statistic_btn = self.find_element(*DashboardPageLocators.STATISTIC_BTN)
        statistic_btn.click()

    def click_atuo_refresh(self):
        auto_refresh = self.find_element(*DashboardPageLocators.AUTO_REFRESH_BTN)
        auto_refresh.click()

    def click_stop_refresh(self):
        stop_refresh = self.find_element(*DashboardPageLocators.STOP_AUTO_REFRESH_BTN)
        stop_refresh.click()

    def click_manual_refresh(self):
        manual_refresh = self.find_element(*DashboardPageLocators.MANUAL_REFRESH_BTN)
        manual_refresh.click()

    def click_heat_map(self):
        heat_map = self.find_element(*DashboardPageLocators.HEAT_MAP_BTN)
        heat_map.click()

    def click_trips(self):
        trips = self.find_element(*DashboardPageLocators.TRIPS_BTN)
        trips.click()

    def click_driver_on_off_duty(self):
        drivers_on_off_duty = self.find_element(*DashboardPageLocators.DRIVERS_ON_OFF_DUTY)
        drivers_on_off_duty.click()

    def navigate_to_trip_history(self):
        self.open('http://69.18.194.208/#/admin/trip_history')

    def navigate_to_drive_duty(self):
        self.open('http://69.18.194.208/#/admin/active_driver')

    def click_analysis_button(self):
        self.find_element(*DashboardPageLocators.ANALYSIS_BTN).click()

    def verify_if_in_dashboard(self):
        try:
            self.find_element(*NavigationPageLocators.DASHBOARD_TAB).click()


        except:
            pass