@adminPage
Feature: user can add an admin in the admin group page
  # Enter feature description here

  Scenario: user can add an admin in the admin group page
    Given a user is logged in
    When user navigates to the admin group page
    Then user clicks the view admin button
    Then user can see the admin list
    Then user clicks the add button in the add admin page
    Then user check the user list in the add admin to group page
    Then user click add button to add admins in the add admin to group page
    Then user can see added admins in the admins of group page