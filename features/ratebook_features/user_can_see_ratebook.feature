@ratebook
Feature: user can see ratebook page
  # Enter feature description here

  Scenario: user can see ratebook page
    Given a user is logged in
    When user navigates to the ratebook page
    Then user can see operr ratebook view all banner in the ratebook page
    Then user can see show all ratebooks and add a new ratebook tabs in the ratebook page
    Then user can see the result table in the ratebook page
    Then user can see the show entries dropdown in the ratebook page
    Then user can see the search text box, search button and searching column dropdown in the ratebook page
    Then user can see the edit button in the ratebook page