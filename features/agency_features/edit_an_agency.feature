@agency
Feature: user can edit a agency
  Scenario: user can edit an existing agencyk
    Given a user is logged in
    When user navigates to the agency page
    Then user sort the table by ID and click the edit button in the agency page
    Then user edits the infomation in the agency info page
    Then user clicks submit button in the agency info page
    Then user can see the edits in the agency page