# Created by mzhang at 9/25/17
  @vehicle
Feature: user can add a vehicle

  Scenario: user cann add vehicle
    Given a user is logged in
    When user navigates to the vehicle page
    Then user clicks add a new vehicle in the vehicle page
    Then user 