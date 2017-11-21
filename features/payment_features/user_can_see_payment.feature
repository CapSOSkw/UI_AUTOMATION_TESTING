@payment
Feature: User can see driver payment page

  Scenario: user can see driver payment page
  Given a user is logged in
    When user navigates to the payment page
    Then user can see companyinfo dropdown in the payment page
    Then user can see agencyname dropdown in the payment page
    Then user can see calendar in the payment page
    Then user can see submit button in the payment page
