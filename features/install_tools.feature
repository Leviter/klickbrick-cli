Feature: Onboarding of new employees and installing tools needed
  Install a set of developer tools and configure according company specific configuration

  Scenario: Git is installed
    Given the command
    When passed the install parameter and the tool "git"
    Then "git" is installed
#    And the git user profile is set up
#    And a git commit template is created

#  Scenario: Pyenv is installed
#    Given the command
#    When passed the install parameter and the tool "pyenv"
#    Then "pyenv" is installed
#    And the global python version is set

#  Scenario: Poetry is installed
#    Given the command
#    When passed the install parameter and the tool "poetry"
#    Then "poetry" is installed
#    And the poetry configuration is updated with an internal repository
