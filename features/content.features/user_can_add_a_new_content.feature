@add_content
Feature: user can add a new content

  Scenario: user adds
    Given a user is logged in
    When user clicks the content navigation button
    Then user can see all content data
    When user clicks the add a new content button
    Then user can add a new content
    Then user edits the content base
    Then user edits the content title
    Then user edits the content description
    Then user edits the content page title
    Then user edits the content page keywords
    Then user edits the content active status
    Then user clicks the content submit button
    Then a new content is added