@adminGroup
Feature: User can add a new group
  # Enter feature description here

  Scenario:user can add a new group
    Given a user is logged in
    When user navigates to the admin group page
    And user navigates to the add a new group page
    Then user can enter username, email, phone, address information in the add a new group page
    Then user can click the active pointer in the add a new group page
    Then user can submit created values in the add a new group page
    Then user can see the created values in the admin group page
