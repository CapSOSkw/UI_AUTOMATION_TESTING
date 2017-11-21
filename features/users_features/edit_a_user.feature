# Created by mzhang at 9/24/17
  @user
Feature: user can edit a user's information
  # Enter feature description here

  Scenario: user can edit a user's information
    Given a user is logged in
    When user navigates to the user page
    Then user sort users by username and clicks edit button in the user page
    Then user edit username, email, firstname, lastname,phone and address information in the user information page
    Then user clicks submit in the user information page
    Then user can see changed user information