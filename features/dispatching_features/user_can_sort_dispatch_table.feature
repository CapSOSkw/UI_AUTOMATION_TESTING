@sort_dispatch
Feature: user can sort table data

  Scenario: user sorts
    Given a user is logged in
    When user clicks the dispatching navigation button
    Then user can see all dispatching data
    When user clicks the dispatch trip id
    Then user can see the dispatch trip-id-sorted table data
    When user clicks the dispatch ts
    Then user can see the dispatch ts-sorted table data
    When user clicks the dispatch rs
    Then user can see the dispatch rs-sorted table data
    When user clicks the dispatch agency name
    Then user can see the dispatch agency-name-sorted table data
    When user clicks the dispatch insurance id
    Then user can see the dispatch insurance-id-sorted table data
    When user clicks the dispatch pickup date
    Then user can see the dispatch pickup-date-sorted table data
    When user clicks the dispatch passenger name
    Then user can see the dispatch passenger-name-sorted table data
    When user clicks the dispatch passenger phone
    Then user can see the dispatch passenger-phone-sorted table data
    When user clicks the dispatch passenger email
    Then user can see the dispatch passenger-email-sorted table data
    When user clicks the dispatch pickup location
    Then user can see the dispatch pickup-location-sorted table data
    When user clicks the dispatch driver
    Then user can see the dispatch driver-sorted table data