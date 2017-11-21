@admin_edit
Feature: user can edit admin

  Scenario: edit admin
    Given a user is logged in
    When user is on the admin page
    Then user can see the all admin data
    When user clicks the username button
    Then user can see username-sorted table data
    When user clicks action button for the first username
    Then user can see all information of this admin
    Then user clears all the information
    Then user edits first name
    Then user edits last name
    Then user edits username
    Then user edits email address
    Then user edits phone number
    Then user rechooses a permission level
    Then user rechooses a company
    Then user rechooses a base
    Then user clicks the admin active status
    Then user clicks submit button on edit page
    Then an admin is changed
