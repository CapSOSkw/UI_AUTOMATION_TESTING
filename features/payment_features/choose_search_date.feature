# Created by mzhang at 9/21/17
  @payment
Feature: Choose payment date range
  Scenario:User can customize the date range for the payment
    Given a user is logged in
    When user navigates to the payment page
    Then  user click the result range textbox and see the daterange dropdown in the payment page
    Then  user can cancel the calendar search in the payment page