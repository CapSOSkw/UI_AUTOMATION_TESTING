@sort_inactive_table
Feature: user can sort table data

  Scenario: user sorts
    Given a user is logged in
    When user is on inactive driver page
    Then user can see inactive driver data
    When user clicks the inactive ID button
    Then user can see inactive ID-sorted table data
    When user clicks the inactive fleet number button
    Then user can see inactive fleet-number-sorted table data
    When user clicks the inactive status button
    Then user can see inactive status-sorted table data
    When user clicks the inactive name button
    Then user can see inactive name-sorted table data
    When user clicks the inactive email button
    Then user can see inactive email-sorted table data
    When user clicks the inactive phone button
    Then user can see inactive phone-sorted table data
    When user clicks the inactive vehicle ID button
    Then user can see inactive vechicle ID-sorted table data
    When user clicks the inactive base button
    Then user can see inactive base-sorted table data
    When user clicks the inactive duty status button
    Then user can see inactive duty-status-sorted table data
    When user clicks the inactive created date button
    Then user can see inactive created-date-sorted table data