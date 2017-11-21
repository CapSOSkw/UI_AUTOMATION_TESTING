
@vehicle
# Created by mzhang at 9/25/17
Feature: user can see vehicle elements in the vehicle page

  Scenario: user can see vehicle elements when navigate to the vehicle page
    Given a user is logged in
    When user navigates to the vehicle page
    Then user can see the Operr Vehicle View All Banner
    Then user can see show all vehicles and add a new vehicle tabs in the vehicle page
    Then user can see the show entries dropdown in the vehicle page
    Then user can see active lable in the vehicle page
    Then user can the result table in the vehicle page
    Then user can see the searching column, searching textbox and searching bottom in the vehicle page
    Then user can see the edit button in the vehicle page