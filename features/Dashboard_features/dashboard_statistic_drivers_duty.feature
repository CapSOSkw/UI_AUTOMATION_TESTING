# Created by KeyuanWu at 9/20/17
Feature: user can check some statistic information
  # Enter feature description here
  @dashboard
  Scenario: statistic data exists
    Given a user is logged in
    When user is in dashboard
    When user navigates to statistic page
    Then user can see statistic data
    When user clicks driver on off duty
    Then user navigates to driver on off duty