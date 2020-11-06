Feature: Get help on the various commands that can be executed
  Get help on a specific command and how to use it

  Scenario: Help is shown
    Given the command
    When passed the help parameter
    Then information is shown about various commands

  Scenario: Help is shown on a specific command
    Given the command
    When passed the help parameter with onboard
    Then information is shown about the onboard parameter
