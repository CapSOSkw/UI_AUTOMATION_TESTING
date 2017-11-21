# Created by mzhang at 9/20/17
  @billing_1
Feature: Choose billing date range
  Scenario:User can customize the date range for the billing
    Given a user is logged in
    When user navigates to the billing page
    Then  user click the result range textbox and see the daterange dropdown in the billing page
    Then  user click today button and the result range shows the right date in the billing page
    Then  user click yesterday button and the result range shows the right date in the billing page
    Then  user click last 7 days button and the result range shows the right date in the billing page
    Then  user click last 30 days button and the result range shows the right date in the billing page
    Then  user click this month button and the result range shows the right date in the billing page
    Then  user click last month button and the result range shows the right date in the billing page
    Then  user can cancel the calendar search in the billing page
