@agency
# Created by mzhang at 9/25/17
Feature: user can add an new agency
  Scenario: user can add a new agency
    Given a user is logged in
    When user navigates to the agency page
    Then user clicks add a new agency tab in the agency info page
    Then user enter an agency type in the agency info page
    Then user enter an agency name in the agency info page
    Then user enter an agency code in the agency info page
    Then user check days in week in the agency info page
    Then user enter worktime start in the agency info page
    Then user enter worktime end in the agency info page
    Then user enter phone in the agency info page
    Then user enter email in the agency info page
    Then user enter address in the agency info page
    Then user enter state in the agency info page
    Then user enter city in the agency info page
    Then user enter zip code in the agency info page
    Then user choose active status in the agency info page
    Then user clicks submit button in the agency info page
    Then user can see the added agency in the agency page
