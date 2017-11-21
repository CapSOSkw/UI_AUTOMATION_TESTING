@ratebook
# Created by mzhang at 9/25/17
Feature: user can add an new ratebook
  Scenario: user can add a new ratebook
    Given a user is logged in
    When user navigates to the ratebook page
    Then user clicks add a new rate book tab in the ratebook page
    Then user select a ratebook type in the ratebook page
    Then user select a fare calculaation type in the ratebook page
    Then user select a company in the ratebook page
    Then user select a base in the ratebook page
    Then user enter per Min Fare in the ratebook page
    Then user enter Minimum Fare in the ratebook page
    Then user enter cancellation fee1 in the ratebook page
    Then user enter base fare in the ratebook page
    Then user select a car type in the ratebook page
    Then user enter per mile fare in the ratebook page
    Then user enter cancellation fee2 in the ratebook page
    Then user select active status in the ratebook page
    Then user clicks submit in the add a new ratebook page
    Then user can see the added ratebook in the ratebook page


