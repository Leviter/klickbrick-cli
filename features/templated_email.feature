Feature: Onboarding of new employees using a templated email
  Create a templated email, using the system default email client, addressed to IT.
  The email will contain all the necessary information for IT to complete onboarding on their end.

  Scenario: The email is generated
    Given the command
    When passed the it-request parameter with firstname "Marcel" and lastname "van den Brink"
    Then name "Marcel" is in the email
    And name "van den Brink" is in the email
