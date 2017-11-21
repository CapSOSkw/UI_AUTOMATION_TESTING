@check_flight
Feature: user can see check flight
  Scenario: user checks
    Given a user is logged in
    When user clicks the flight check navigation button
    Then user enters airline
    Then user enters flight number
    Then user enters departing date
    Then user clicks flight check search button
    Then user can see the flight information