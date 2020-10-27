Feature: Onboarding of new employees using a templated email
  Create a templated email, using the system default email client, addressed to IT.
  The email will contain all the necessary information for IT to complete onboarding on their end.

  Scenario: The email is generated
    Given the command
    When passed the it-request parameter
    Then an email is generated
