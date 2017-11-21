@admin
Feature: user can see admin page

  Scenario: All elements in admin page exist
    Given a user is logged in
    When user is on the admin page
    Then user can see the all admin data