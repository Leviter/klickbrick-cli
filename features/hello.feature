Feature: Hello World

  Scenario: the program greets the world
    When I start the program with the hello parameter
    Then it prints "hello world"

  Scenario: the program greets us personally
    When I start the program with the hello parameter and a name parameter having the value Marcel
    Then it prints "hello Marcel"
