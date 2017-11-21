@payment
Feature: user can submit search critiera

  Scenario: user can submit search criteria
    Given a user is logged in
    When user navigates to the payment page
    Then user can choose company info dropdown in the payment page
    Then user can choose base info dropdown in the payment page
    Then user can choose agency name dropdown in the payment page
    Then user can choose driver info dropdown in the payment page
    Then user can submit search criteria and see the result table in the payment page
    Then user can see export detail, export summary button, and approve button in the payment page
