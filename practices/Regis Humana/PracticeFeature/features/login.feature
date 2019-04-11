Feature: Login Feature
  As as AT09 engineer
  I want to test logging
  To verify all Login functionally

  #Scenario: Successful login with an existent account
    #Given I open the browser at: "https://www.google.com"

  #Scenario: Verify using an existent account the login is Successful
   # Given I open the browser at: "https://www.AT09.com"

#  Scenario Outline: Successful login with an existent account
#    Given I open the browser at: : "<url>"
#
#    Examples:
#        | url |
#        | www.google.com |
#        | www.google.es |
  Background:
    Given I have the calculator open

  Scenario: Addition test case
    #Given I have the calculator open
    When I put first number: 50
    And I press + button
    And I put second number: 10
    And I press = button to perform the operation
    Then I should have 60 as a sum

  Scenario Outline: Rest operations
    #Given I have the calculator open
    When I put first number: <first_num>
    And I press <operator> button
    And I put second number: <second_num>
    And I press = button to perform the operation
    Then I should have <result> as a sum
    Examples:
      |first_num|second_num|operator|result|
      | 50 | 10 | - | 40 |
      | 2  | 5  | * | 10 |
      | 10 | 5  | / | 2  |
      | 10 | 5  | + | 15 |

  Scenario: Divide by zero test case
    #Given I have the calculator open
    When I put first number: 50
    And I press / button
    And I put second number: 0
    And I press = button to perform the operation
    Then I should have Divide Zero Exception message

  Scenario: Addition test case
    #Given I have the calculator open
    When I will perform the operation  50 + 10
    Then I should have 60 as a sum