@edit_inactive
Feature: user can edit inactive driver data

  Scenario: user edits
    Given a user is logged in
    When user is on inactive driver page
    Then user can see inactive driver data
    When user clicks the inactive username button
    Then user can see inactive username-sorted table data
    When user clicks the inactive action edit button for the first username
    Then user can see all information of this inactive user
    Then user clears the inactive driver information
    Then user edits the inactive driver first name
    Then user edits the inactive driver last name
    Then user edits the inactive driver username
    Then user edits the inactive driver email
    Then user edits the inactive driver phone number
    Then user edits the inactive driver date of birth
    Then user edits the inactive driver gender
    Then user edits the inactive driver country of origin
    Then user edits the inactive driver driving experience
    Then user edits the inactive driver type
    Then user edits the inactive driver affiliated company name
    Then user edits the inactive driver affiliated based name
    Then user clicks the inactive driver base approved active
    Then user clicks the inactive driver operr status approve
    Then user edits the inactive driver license number
    Then user edits the inactive driver license class
    Then user edits the inactive driver license state
    Then user edits the inactive driver license start date
    Then user edits the inactive driver license expire date
    Then user edits the inactive driver TLC FHV license number
    Then user edits the inactive driver TLC FHV license start date
    Then user edits the inactive driver TLC FHV license expire date
    Then user edits the inactive driver background check start date
    Then user edits the inactive driver background check expire date
    Then user edits the inactive driver driving record start date
    Then user edits the inactive driver driving record expire date
    Then user edits the inactive driver drug screen start date
    Then user edits the inactive driver drug screen expire date
    Then user edits the inactive driver vehicle info
    Then user edits the inactive cross county
    Then user clicks inactive driver page submit button
    Then an inactive driver is changed