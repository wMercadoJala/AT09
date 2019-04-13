@holaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
Feature: Create a new gmail account
@AT09 @regression
  Scenario: Creation Test Case
    Given Gmail page opened
    When I fill first_name: Valeria
    And I fill last_name: Loza
    And I fill user_name: valeria.loza@gmail.com
    And I fill password: mypassword
    And I fill confirm_pws
    And I fill birthday month: enero
    And I fill birthday day: 1
    And I fill birthday year: 2000
    And I fill gender: female
    And I fill country_code: +591
    And I fill phone_number: 75555555
    And I fill current_mail: valeria.loza@hotmail.com
    And I press the Register Button
    Then I get the successful message

  Scenario: Creation Test Case without first name
    Given Gmail page opened
    When I fill last_name: Caballero
    And I fill user_name: v.loza@gmail.com
    And I fill password: mypassword
    And I fill confirm_pws
    And I fill birthday month: enero
    And I fill birthday day: 1
    And I fill birthday year: 2000
    And I fill gender: female
    And I fill country_code: +591
    And I fill phone_number: 75555554
    And I fill current_mail: valeria.loza@hotmail.com
    And I press the Register Button
    Then I get the failed message

  Scenario: Creation Test Case without user name
    Given Gmail page opened
    When I fill first_name: Vicente
    And I fill last_name: Caballero
    And I fill password: mypassword
    And I fill confirm_pws
    And I fill birthday month: enero
    And I fill birthday day: 1
    And I fill birthday year: 2000
    And I fill gender: female
    And I fill country_code: +591
    And I fill phone_number: 75555554
    And I fill current_mail: valeria.l@hotmail.com
    And I press the Register Button
    Then I get the failed message

Scenario Outline: Creation with diferent values Test Case
    Given Gmail page opened
    When I fill first_name: <first>
    And I fill last_name: <last>
    And I fill user_name: <user_name>
    And I fill password: <password>
    And I fill confirm_pws
    And I fill birthday month: <month>
    And I fill birthday day: <day>
    And I fill birthday year: <year>
    And I fill gender: <gender>
    And I fill country_code: <country_code>
    And I fill phone_number: <phone_number>
    And I fill current_mail: <current_mail>
    And I press the Register Button
    Then I get the successful message
  Examples:
    | first | last | user_name | password |month | day | year | gender | country_code | phone_number | current_mail |
    |Vicente| Caballero|v.caballero@gmail.com|pwsvicente|febrero|10|2001|male|+55         |76666666      |v.l@hotmail.com|

