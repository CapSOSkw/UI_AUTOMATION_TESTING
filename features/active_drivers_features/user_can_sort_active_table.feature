@sort_active_table
Feature: user can sort table data

  Scenario: user sorts
    Given a user is logged in
    When user clicks the active drivers navigation button
    Then user can see active driver data
    When user clicks the active ID button
    Then user can see active ID-sorted table data
    When user clicks the active fleet number button
    Then user can see active fleet-number-sorted table data
    When user clicks the active status button
    Then user can see active status-sorted table data
    When user clicks the active name button
    Then user can see active name-sorted table data
    When user clicks the active email button
    Then user can see active email-sorted table data
    When user clicks the active phone button
    Then user can see active phone-sorted table data
    When user clicks the active vehicle ID button
    Then user can see active vechicle ID-sorted table data
    When user clicks the active base button
    Then user can see active base-sorted table data
    When user clicks the active duty status button
    Then user can see active duty-status-sorted table data
    When user clicks the active created date button
    Then user can see active created-date-sorted table data