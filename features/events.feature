Feature: Validate the handling of events sent from the KlickBrick application

  Scenario: events are being sent from the application
    Given a running server to receive events
    When running the application with the help command
    Then the event contains the command
    And the event contains the parameters
    And the event contains the OS

#  Scenario: application keeps on running even when no receiving server is running
#    When
#    Then it prints "hello Marcel"
