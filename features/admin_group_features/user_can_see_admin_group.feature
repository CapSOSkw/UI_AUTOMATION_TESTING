@adminGroup
Feature: user can see admin group

  Scenario: user can see admin group page
    Given a user is logged in
    When user navigates to the admin group page
    Then user can see the show_all_admin_group and add_a_new_group tabs in the admin group page
    Then user can see the show entries dropdown and text in the admin group page
    Then user can see the action buttons in the admin group page

##### could not locate the table
