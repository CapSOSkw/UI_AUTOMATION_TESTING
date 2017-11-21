
# Created by KeyuanWu at 9/20/17
Feature: user can check some statistic information
  # Enter feature description here
@dashboard
  Scenario: statistic data exists
    Given a user is logged in
    When user is in dashboard
    When user navigates to statistic page
    Then user can see statistic data
    When user clicks auto refresh button
    Then webpage keeps refreshing
    When user clicks stop auto refresh button
    Then webpage stops refreshing
    When user clicks manual refresh button
    Then webpage refreshes once
    When user clicks heat map
    Then user can see heat map
    When user clicks trips button
    Then user navigates to trip history page