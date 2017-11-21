@edit_base
Feature: user can edit base

  Scenario: user edits
    Given a user is logged in
    When user clicks the base navigation button
    Then user can see all bases data
    When user clicks action button for the first base
    Then user can edit the base
    Then user clear the base data
    Then user edits the base company
    Then user edits the base base name
    Then user edits the base base type
    Then user edits the base fare type
    Then user edits the base federal tax id
    Then user edits the base address
    Then user edits the base state
    Then user edits the base city
    Then user edits the base zipcode
    Then user edits the base main contact
    Then user edits the base business phone
    Then user edits the base business fax
    Then user clicks the base tracking mode active button
    Then user clicks the base status active button
    Then user edits the base TLC license number
    Then user edits the base TLC license start date
    Then user edits the base TLC license exp date
    Then user edits the base auto liability amount
    Then user edits the base auto operr certificate holder
    Then user edits the base auto self insured
    Then user edits the base auto operr additional insured
    Then user edits the base auto name afford coverage
    Then user edits the base auto insurance start date
    Then user edits the base auto insurance exp date
    Then user edits the base general liability amount
    Then user edits the base general operr certificate holder
    Then user edits the base general self insured
    Then user edits the base general operr additional insured
    Then user edits the base general name afford coverage
    Then user edits the base general insurance start date
    Then user edits the base general insurancce exp date
    Then user edits the base IRS business name
    Then user edits the base TIN EIN SNN
    Then user edits the base federal id w9 start date
    Then user edits the base federal id w9 exp date
    Then user edits the base worker compensation amount
    Then user edits the base worker compensation start date
    Then user edits the base worker compensation exp date
    Then user edits the base training attest start date
    Then user edits the base training attest exp date
    Then user edits the base schedule a start date
    Then user edits the base schedule a exp date
    Then user edits the base schedule b start date
    Then user edits the base schedule b exp date
    Then user edits the base aetna start date
    Then user edits the base aetna exp date
    Then user edits the base insurance endorsement start date
    Then user edits the base insurance endorsement exp date
    Then user edits the base NYCT start date
    Then user edits the base NYCT exp date
    Then user edits the base service agreement start date
    Then user edits the base service agreement exp date
    Then user edits the base wellcare start date
    Then user edits the base wellcare exp date
    Then user clicks the base submit button
    Then a new base is added