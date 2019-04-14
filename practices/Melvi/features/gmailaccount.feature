Feature: Create a new gmail account
Background:
  Given Gmail page opened

  Scenario: Creation Test Case
    When I fill first_name: Valeria
    And I fill last_name: Loza
    And I fill user_name: valeria.loza@gmail.com
    And I fill password: mypassword
    And I fill confirm_pws: mypassword
    And I fill birthday month: Enero
    And I fill birthday day: 1
    And I fill birthday year: 2000
    And I fill gender: female
    And I fill country_code: +591
    And I fill phone_number: 75555555
    And I fill current_mail: valeria.loza@hotmail.com
    And I press the Register Button
    Then I get the successful message

  Scenario: Creation Test Case without first name
    When I fill last_name: Caballero
    And I fill user_name: v.loza@gmail.com
    And I fill password: mypassword
    And I fill confirm_pws: mypassword
    And I fill birthday month: Enero
    And I fill birthday day: 1
    And I fill birthday year: 2000
    And I fill gender: female
    And I fill country_code: +591
    And I fill phone_number: 75555554
    And I fill current_mail: valeria.loza@hotmail.com
    And I press the Register Button
    Then I get the Missing first name message

  Scenario: Creation Test Case without last name
    When I fill first_name: Valeria
    And I fill user_name: valeria.loza@gmail.com
    And I fill password: mypassword
    And I fill confirm_pws: mypassword
    And I fill birthday month: Enero
    And I fill birthday day: 1
    And I fill birthday year: 2000
    And I fill gender: female
    And I fill country_code: +591
    And I fill phone_number: 75555555
    And I fill current_mail: valeria.loza@hotmail.com
    And I press the Register Button
    Then I get the Missing last name message

  Scenario: Creation Test Case with out password
    When I fill first_name: Valeria
    And I fill last_name: Loza
    And I fill user_name: valeria.loza@gmail.com
    And I fill confirm_pws: mypassword
    And I fill birthday month: Enero
    And I fill birthday day: 1
    And I fill birthday year: 2000
    And I fill gender: female
    And I fill country_code: +591
    And I fill phone_number: 75555555
    And I fill current_mail: valeria.loza@hotmail.com
    And I press the Register Button
    Then I get the Missing password message

  Scenario: Creation Test Case with out confirm password
    When I fill first_name: Valeria
    And I fill last_name: Loza
    And I fill user_name: valeria.loza@gmail.com
    And I fill password: mypassword
    And I fill birthday month: Enero
    And I fill birthday day: 1
    And I fill birthday year: 2000
    And I fill gender: female
    And I fill country_code: +591
    And I fill phone_number: 75555555
    And I fill current_mail: valeria.loza@hotmail.com
    And I press the Register Button
    Then I get the Missing password confirmation message

  Scenario: Creation Test Case with confirm password does not match
    When I fill first_name: Valeria
    And I fill last_name: Loza
    And I fill user_name: valeria.loza@gmail.com
    And I fill password: mypassword
    And I fill confirm_pws: mypasswor
    And I fill birthday month: Enero
    And I fill birthday day: 1
    And I fill birthday year: 2000
    And I fill gender: female
    And I fill country_code: +591
    And I fill phone_number: 75555555
    And I fill current_mail: valeria.loza@hotmail.com
    And I press the Register Button
    Then I get the Password confirmation does not match password message

  Scenario: Creation Test Case without user name
    When I fill first_name: Vicente
    And I fill last_name: Caballero
    And I fill password: mypassword
    And I fill confirm_pws: mypassword
    And I fill birthday month: Enero
    And I fill birthday day: 1
    And I fill birthday year: 2000
    And I fill gender: female
    And I fill country_code: +591
    And I fill phone_number: 75555554
    And I fill current_mail: valeria.l@hotmail.com
    And I press the Register Button
    Then I get the Missing user name message

Scenario Outline: Creation with different values Test Case
    When I fill first_name: <first>
    And I fill last_name: <last>
    And I fill user_name: <user_name>
    And I fill password: <password>
    And I fill confirm_pws: <confirm_pws>
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
    | first | last | user_name | password |confirm_pws|month | day | year | gender | country_code | phone_number | current_mail |
    |Vicente| Caballero|v.caballero@gmail.com|pwsvicente|pwsvicente|Febrero|10|2001|male|+55         |76666666      |v.l@hotmail.com|

  Scenario: Creation Test Case with invalid email
    When I fill first_name: Valeria
    And I fill last_name: Loza
    And I fill user_name: valeria.loza@gmail.com
    And I fill password: mypassword
    And I fill confirm_pws: mypassword
    And I fill birthday month: Enero
    And I fill birthday day: 1
    And I fill birthday year: 2000
    And I fill gender: female
    And I fill country_code: +591
    And I fill phone_number: 75555555
    And I fill current_mail: valeria.lozahotmail.com
    And I press the Register Button
    Then I get the invalid email message

  Scenario: Creation Test Case with invalid birth date
    When I fill first_name: Valeria
    And I fill last_name: Loza
    And I fill user_name: valeria.loza@gmail.com
    And I fill password: mypassword
    And I fill confirm_pws: mypassword
    And I fill birthday month: Febrero
    And I fill birthday day: 31
    And I fill birthday year: 2000
    And I fill gender: female
    And I fill country_code: +591
    And I fill phone_number: 75555555
    And I fill current_mail: valeria.lozahotmail.com
    And I press the Register Button
    Then I get the invalid birthday date message

  Scenario: Creation Test Case with future birth date
    When I fill first_name: Valeria
    And I fill last_name: Loza
    And I fill user_name: valeria.loza@gmail.com
    And I fill password: mypassword
    And I fill confirm_pws: mypassword
    And I fill birthday month: Febrero
    And I fill birthday day: 14
    And I fill birthday year: 2020
    And I fill gender: female
    And I fill country_code: +591
    And I fill phone_number: 75555555
    And I fill current_mail: valeria.lozahotmail.com
    And I press the Register Button
    Then I get the invalid birthday date message

 Scenario: Creation Test Case with invalid phone number
    When I fill first_name: Valeria
    And I fill last_name: Loza
    And I fill user_name: valeria.loza@gmail.com
    And I fill password: mypassword
    And I fill confirm_pws: mypassword
    And I fill birthday month: Enero
    And I fill birthday day: 1
    And I fill birthday year: 2000
    And I fill gender: female
    And I fill phone_number: 755555r5
    And I fill current_mail: valeria.loza@hotmail.com
    And I press the Register Button
    Then I get the Missing select country code message

 Scenario: Creation Test Case with invalid phone number
    When I fill first_name: Valeria
    And I fill last_name: Loza
    And I fill user_name: valeria.loza@gmail.com
    And I fill password: mypassword
    And I fill confirm_pws: mypassword
    And I fill birthday month: Enero
    And I fill birthday day: 1
    And I fill birthday year: 2000
    And I fill gender: female
    And I fill country_code: +591
    And I fill phone_number: 755555r5
    And I fill current_mail: valeria.loza@hotmail.com
    And I press the Register Button
    Then I get the Phone number should be a number message
