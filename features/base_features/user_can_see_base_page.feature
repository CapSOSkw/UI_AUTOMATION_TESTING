@see_base
# Created by KeyuanWu at 9/26/17
Feature: user can see base page

  Scenario: all elements exist
    Given a user is logged in
    When user clicks the base navigation button
    Then user can see all bases data
    