@see_inactive_driver
Feature: user can see inactive driver page

  Scenario: all elements on inactive driver page exist
    Given a user is logged in
    When user is on inactive driver page
    Then user can see inactive driver data
