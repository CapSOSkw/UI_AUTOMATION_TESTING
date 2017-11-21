@vehicle
Feature: user can edit a vehicle's information
  # Enter feature description here

  Scenario: user can edit a vehicle's information
    Given a user is logged in
    When user navigates to the vehicle page
    Then user sort users by VIN and clicks edit button in the vehicle page
    Then user edit vehicle information in the vehicle information page
    Then user clicks submit in the vehicle information page
    Then user can user search textbox and find the edits in the vehicle page