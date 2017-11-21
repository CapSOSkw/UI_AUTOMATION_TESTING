@add_dispatch
Feature: user can add a new booking

  Scenario:
    Given a user is logged in
    When user clicks the dispatching navigation button
    Then user can see all dispatching data
    When user clicks add a new booking
    Then user can see dispatching edit page
    Then user edits the dispatch affiliated company name
    Then user edits the dispatch affiliated base name
    Then user edits the dispatch first name
    Then user edits the dispatch last name
    Then user edits the dispatch phone number
    Then user edits the dispatch driver auto assign
    Then user edits the dispatch trip type
    Then user edits the dispatch trip info
    Then user clicks dispatch submit button
    Then a new dispatch booking is added