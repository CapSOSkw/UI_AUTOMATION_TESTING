@admin
Feature: user can see sorted table data

  Scenario: user sorts status
    Given a user is logged in
    When user is on the admin page
    Then user can see the all admin data
    When user clicks the status button
    Then user can see status-sorted table data
    When user clicks the username button
    Then user can see username-sorted table data
    When user clicks the email button
    Then user can see email-sorted table data
    When user clicks the phone button
    Then user can see phone-sorted table data
    When user clicks the 2nd phone button
    Then user can see 2nd-phone-sorted table data
    When user clicks the admin level button
    Then user can see admin-level-sorted table data
    When user clicks the company button
    Then user can see company-sorted table data
    When user clicks the base button
    Then user can see base-sorted table data
    When user clicks the name button
    Then user can see name-sorted table data

