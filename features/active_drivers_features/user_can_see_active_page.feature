@see_active_driver
Feature: user can see active driver page

  Scenario: all elements on active drivers page exist
    Given a user is logged in
    When user clicks the active drivers navigation button
    Then user can see active driver data