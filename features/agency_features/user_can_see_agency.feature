@agency
Feature: user can see agency
  # Enter feature description here

  Scenario: user can see agency page
    Given a user is logged in
    When user navigates to the agency page
    Then user can see operr agency view all banner in the agency page
    Then user can see show all agencys and add a new agency tabs in the agency page
    Then user can see the show entries dropdown in the agency page
    Then user can see the search text box, search button and searching column dropdown in the agency page
    Then user can see the edit button in the agency page