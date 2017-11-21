@see_content
Feature: user can see content page
  Scenario: all elements exist
    Given a user is logged in
    When user clicks the content navigation button
    Then user can see all content data