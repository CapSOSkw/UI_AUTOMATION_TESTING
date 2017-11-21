@ratebook
Feature: user can edit a ratebook
  Scenario: user can edit an existing ratebookk
    Given a user is logged in
    When user navigates to the ratebook page
    Then user click the edit button in the ratebook page
    Then user edits the infomation in the ratebook info page
    Then user clicks submit button in the ratebook info page
    Then user can see the edits in the ratebook page