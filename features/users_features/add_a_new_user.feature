# Created by mzhang at 9/24/17]
  @user
Feature: user can add a user
  Scenario:user can add a user
    Given a user is logged in
    When user navigates to the user page
    Then user clicks add a new user in the user page
    Then user enter username,email,password,first name, last name, phone, address in the user information page
    Then user choose active status in the user information page
    Then user click submit button in the user information page
    Then user can see the added user
