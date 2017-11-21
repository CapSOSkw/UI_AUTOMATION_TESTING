@see_flight
Feature: user can see flight check page

  Scenario: all elements exist
    Given a user is logged in
    When user clicks the flight check navigation button
    Then user can see flight check page