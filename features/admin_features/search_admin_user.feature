@admin
Feature: User can search an admin

  Scenario: user is searching on the admin page
    Given a user is logged in
    When user is on the admin page
    Then user can see the all admin data
    Then user types a text in the search box
	Then user clicks the search button in the admin page
	Then result containing text should display