Feature: Hello World

  Scenario: the program greets us
    When I start the program without any parameters
    Then it prints "hello world"

  Scenario: the program greets us personally
    When I start the program with a name parameter having the value Marcel
    Then it prints "hello Marcel"
