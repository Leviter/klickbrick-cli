Feature: Onboarding of new employees using a checklist
  Generate a checklist document in Markdown
  with all of the manual onboarding activities the new employee needs to complete.

  Scenario: The checklist is generated
    Given the command
    When passed the checklist parameter
    Then a markdown file is created
