@add_company_test
Feature: user can add a new company

  Scenario: user adds
    Given a user is logged in
    When user clicks the company navigation button
    Then user can see all companies data
    When user clicks the add a new company button
    Then user can add a new company
    Then user edits the company name
    Then user edits the days in week
    Then user edits the start worktime
    Then user edits the end worktime
    Then user edits the phone number
    Then user edits the email
    Then user edits the address
    Then user edits the state
    Then user edits the city
    Then user edits the zipcode
    Then user chooses active status
    Then user clicks submit button on add a new company page
    Then a new company is added