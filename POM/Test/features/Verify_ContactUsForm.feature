Feature: Contact Us Form
   As a user,
   I want to be able to send a question, through the form in the Contact Us section


@Regression
  Scenario: Send a Question or Doubt, through the form in Contact Us
    Given I am on the Automation test logged in
    When  I select the Contact Us option in the footer of the page,
    And  Fill form name "gonza", email "gonza.mol@darwoft.com", Enquiry "Pueden regalarme puntos"
    Then I want to verify that my question has been sent successfully


@Regression
  Scenario: Send a Question or Doubt, through the form in Contact Us with an empty form
    Given I am on the Automation test logged in
    When  I select the Contact Us option in the footer of the page,
    And  I do not complete any of the fields
    Then I want to verify that the validation errors are displayed in each of the fields