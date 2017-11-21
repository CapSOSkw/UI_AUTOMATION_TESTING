@billing
Feature: User can see elements in the Billing page

Scenario: Elements in Billing page exists
  Given a user is logged in
  When user navigates to the billing page
  Then user can see companyinfo dropdown in the billing page
  Then user can see agencyname dropdown in the billing page
  Then user can see calendar in the billing page
  Then user can see submit button in the billing page