@see_dispatch
Feature: user can see dispatching page

  Scenario: all elements exist
    Given a user is logged in
    When user clicks the dispatching navigation button
    Then user can see all dispatching data
