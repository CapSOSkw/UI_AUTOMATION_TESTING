@see_company
Feature: user can see company page

  Scenario: all elements exist
    Given a user is logged in
    When user clicks the company navigation button
    Then user can see all companies data