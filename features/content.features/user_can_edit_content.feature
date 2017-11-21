@edit_content
Feature: user can edit a content

  Scenario: user edits
    Given a user is logged in
    When user clicks the content navigation button
    Then user can see all content data
    When user clicks the action edit button for the first content
    Then user can edit a content
    Then user clears the content information
    Then user edits the content base
    Then user edits the content title
    Then user edits the content description
    Then user edits the content page title
    Then user edits the content page keywords
    Then user edits the content active status
    Then user clicks the content submit button
    Then a content is changed