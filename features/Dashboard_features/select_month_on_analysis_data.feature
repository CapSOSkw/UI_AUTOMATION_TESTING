Feature: user can see different data by choosing date
@dashboard
  Scenario: user can select data
    Given a user is logged in
    When user is in dashboard
    When user is in analysis page
    When user clicks 3-month button
    Then user can see 3-month data
    When user clicks 6-month button
    Then user can see 6-month data
    When user clicks 12-month button
    Then user can see 12-month data