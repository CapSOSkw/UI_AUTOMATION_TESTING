@admin_add
Feature: user can add a new admin

  Scenario: add admin
    Given a user is logged in
    When user is on the admin page
    Then user can see the all admin data
    When user clicks add a new admin button
    Then user can add a new admin
    Then user enters first name
    Then user enters last name
    Then user enters username
    Then user enters email address
    Then user creates password
    Then user enters valid phone number
    Then user chooses a permission level
    Then user chooses a company
    Then user chooses a base
    Then user clicks active button
    Then user submits
    Then a new admin is added

