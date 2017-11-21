# Created by mzhang at 9/22/17
  @adminGroup
Feature: user can edit the admin group information

  Scenario: user can edit admin group information
    Given a user is logged in
    When user navigates to the admin group page
    Then user clicks edit admin group page in the admin group page
    Then user can see the admin detail information and admin information in the admin edit page
    Then user edit username, email, phone, address information in the admin group page
    Then use change status in the admin in the admin group page
    Then user click submits in the admin group page
    Then the edits should be saved in the admin group page in the admin group page
