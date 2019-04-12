Feature: Create_account_Gmail Feature
  As a AT09 engineer
  I want to test create account in gmail
  In order to verify all Create functionality
  Background:
    Given I open the form for create gmail account

 Scenario: Verify the form create account
    When I get form create account
    Then I receive status code 200

  Scenario: Create a new successful account
    When I fill Cxristian in First Name field
    And I fill Lujan in Last Name field
    And I fill cxristian.lujan05@gmail.com in User Name field
    And I fill qwerty123 in Pass field
    And I fill confirm _pass in Confirm Pass field
    And I fill august in month Birthday field
    And I fill 05 in day Birthday field
    And I fill 2000 in year Birthday field
    And I fill +591 in Code field
    And I fill male in Gender field
    And I fill 78345290 in mobile phone field
    And I fill cristian.fundacion-jala.org in Current Email field
    And I press next button
    Then Successfully created account

  Scenario Outline: Create a new successful account only required fields
    When I fill <first> in First Name field
    And I fill <last> in Last Name field
    And I fill <user_name> in User Name field
    And I fill <password> in Pass field
    And I fill confirm _pass in Confirm Pass field
    And I press next button
    Then Successfully created account

    Examples:
      | first | last | user_name | password |
      | Cxristian | Lujan | cxristian.lujan05@gmail.com | qwerty123|

  Scenario Outline: Create a new successful account only required fields
    When I fill <first> in First Name field
    And I fill <last> in Last Name field
    And I fill <user_name> in User Name field
    And I fill <password> in Pass field
    And I fill confirm _pass in Confirm Pass field
    And I press next button
    Then fail created account

    Examples:
      | first | last | user_name | password |
      || Lujan | cxristian.lujan05@gmail.com | qwerty123|
      | Cxristian || cxristian.lujan05@gmail.com | qwerty123|
      | Cxristian | Lujan || qwerty123|
      | Cxristian | Lujan | cxristian.lujan05@gmail.com ||

  Scenario: Create a new account with an user same
    When I fill Carlos in First Name field
    And I fill Villca in Last Name field
    And I fill carlitos.vil005@gmail.com in User Name field
    And I fill qwerty123 in Pass field
    And I fill confirm _pass in Confirm Pass field
    And I press next button
    Then I should have Exist that User

  Scenario Outline: Successful Create a new account
    When I fill <first> in First Name field
    And I fill <last> in Last Name field
    And I fill <user_name> in User Name field
    And I fill <password> in Pass field
    And I fill confirm _pass in Confirm Pass field
    And I fill <month> in month Birthday field
    And I fill <day> in day Birthday field
    And I fill <year> in year Birthday field
    And I fill <country_code> in Gender field
    And I fill <gender> in Gender field
    And I fill <phone> in mobile phone field
    And I fill <current_email> in Current Email field
    And I press next button
    Then Successfully created account

  Examples:
    | first | last | user_name | password | month | day | year | gender | country_code| phone | current_email|
    | Cxristian | Lujan | cxristian.lujan05@gmail.com | qwerty123| august | 05 | 2000 | male | +591 | 78345290 | cristian.c@fundacion-jala.org |
    | Julieta | Perez | july.per35@gmail.com | zxc563| february | 20 | 1999 | female | +591 | 78356890 | julia.c@fundacion-jala.org |