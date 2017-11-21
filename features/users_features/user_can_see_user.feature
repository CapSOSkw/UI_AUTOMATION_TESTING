@see_user
Feature: user can see user page
  # Enter feature description here

  Scenario: user can see user page
    Given a user is logged in
    When user navigates to the user page
    Then user can see operr users view all banner in the users page
    Then user can see show all users and add a new user tabs in the users page
    Then user can see the result table in the users page
    Then user can see the active lable in the users page
    Then user can see the show entries dropdown in the users page
    Then user can see the search text box and searching column dropdown in the users page
    Then user can see the edit button in the users page