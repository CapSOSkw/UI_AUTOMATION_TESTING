@sort_base
Feature: user can sort table data

  Scenario: user sorts
    Given a user is logged in
    When user clicks the base navigation button
    Then user can see all bases data
    When user clicks the base status button
    Then user can see base status-sorted table data
    When user clicks the base base name button
    Then user can see base based-name-sorted table data
    When user clicks the base base type button
    Then user can see base base-type-sorted table data
    When user clicks the base company button
    Then user can see base company-sorted table data
    When user clicks the base fare type button
    Then user can see base fare-type-sorted table data
