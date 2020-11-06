Feature: Initialise a git project
  Help the developer to set up a new project

  Scenario: Help is shown
    Given the command
    When passed the init parameter and a project dummy and directory ./projects
    Then the directory ./projects/dummy for the project is created
    And correctly initialised

