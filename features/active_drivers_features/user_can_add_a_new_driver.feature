@add_new_active
Feature: user can add a new active driver

  Scenario: user adds
    Given a user is logged in
    When user clicks the active drivers navigation button
    Then user can see active driver data
    When user clicks add a new driver button
    Then user can add a new driver
    Then user edits the active driver first name
    Then user edits the active driver last name
    Then user edits the active driver username
    Then user edits the active driver email
    Then user edits the active driver password
    Then user edits the active driver phone number
    Then user edits the active driver date of birth
    Then user edits the active driver gender
    Then user edits the active driver country of origin
    Then user edits the active driver driving experience
    Then user edits the active driver type
    Then user edits the active driver affiliated company name
    Then user edits the active driver affiliated based name
    Then user edits the active driver dsp percent
    Then user edits the active driver base percent
    Then user edits the active driver driver percent
    Then user edits the active driver reserve percent
    Then user clicks the active driver base approved active
    Then user edits the active driver license number
    Then user edits the active driver license class
    Then user edits the active driver license state
    Then user edits the active driver license start date
    Then user edits the active driver license expire date
    Then user edits the active driver TLC FHV license number
    Then user edits the active driver TLC FHV license start date
    Then user edits the active driver TLC FHV license expire date
    Then user edits the active driver background check start date
    Then user edits the active driver background check expire date
    Then user edits the active driver driving record start date
    Then user edits the active driver driving record expire date
    Then user edits the active driver drug screen start date
    Then user edits the active driver drug screen expire date
    Then user edits the active driver vehicle info
    Then user edits the active cross county
    Then user clicks active driver page submit button
    Then an active driver is changed
