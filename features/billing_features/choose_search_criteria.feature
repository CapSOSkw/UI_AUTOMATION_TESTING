@billing
Feature: user can submit search critiera

  Scenario: user can submit search criteria
    Given a user is logged in
    When user navigates to the billing page
    Then user can choose company info dropdown in the billing page
    Then user can choose base info dropdown in the billing page
    Then user can choose agency name dropdown in the billing page
    Then user can choose driver info dropdown in the billing page
    Then user can submit search criteria and see the result table in the billing page


