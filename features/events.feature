Feature: Validate the handling of events sent from the KlickBrick application

  Scenario: application continues when events cannot be sent
    Given a non-running server to receive events
    When running the application with the help command
    Then a timout is logged
