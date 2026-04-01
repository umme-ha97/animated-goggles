Feature: signup/Login functionality for a company

  Scenario: To signup the website
    Given User opens the url for the website
    Then User is on sign in page
    Then User enters "firstname" name
    Then User enters email as "testemail@gmail.com" email
    Then User enters "ABC" company
    Then User enters "software engineer" as job title
    Then User selects "india" for country code
    Then User enters "8123456789" phone number
    Then User selects the service from the dropdown
    Then User clicks on submit button



