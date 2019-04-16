Feature: Create new account of gmail
  As a common user
  I want to create a new account
  In order to verify the creation of  an account successful

  Scenario Outline: Successful creation account sending only required fields
    Given I am looking at the creation account page
    When I fill <first name> in first name field
    And I fill the <last name> in last name field
    And I fill the <username> in username
    And  I fill the <password> in Create a password field
    Then I should see the message: Account created successfully

    Examples:
      | first name | last name | username | password |
      |  Areliez | Vargas | areliez.vargas | Control123* |
      |  Areliez | Vargas | areliez.123 | Control123* |
      |  Areliez | Vargas | Are456 | Control123*      |
      |  Areliez | Vargas | areliez.vargas.123 | Control123* |
      |  Areliez | Vargas | areliez| Control123* |
      |  Areliez | Vargas | areliez.vargas | Control8 |

  Scenario Outline: Successful creation account all fields
    Given I am looking at the creation account page
    When I fill <first name> in first name field
    And I fill the <last name> in last name field
    And I fill the <username> in username
    And I fill the <password> in Create a password field
    And I select <month> in Birthday dropdown
    And I fill <day> in Day field
    And I fill <year> in Year field
    And I select <gender> in Gender dropdown
    And I select <Country> in Country
    And I fill <cellphone> in Mobile phone field
    And I fill <current email> in Your current email address field
    And I click on "Sign Up" button
    Then I should see the message: Account created successfully

    Examples:
      | first name | last name | username | password | month | day | year | gender| Country | cellphone | current email|
      |  Maria     | Vargas    | maria.vargas | Control123* | July | 1 | 2000 |    F  | Bolivia | 77777777 | maria.vargas@gmail.com |
      |  Miguel    | Vargas | miguel.vargas | Control123* | September | 30 | 1991 |  M  | Bolivia | 77777777 | miguel@gmail.com |


  Scenario Outline: Successful creation account without gender field
    Given I am looking at the creation account page
    When I fill <first name> in first name field
    And I fill the <last name> in last name field
    And I fill the <username> in username
    And I fill the <password> in Create a password field
    And I select <month> in Birthday dropdown
    And I fill <day> in Day field
    And I fill <year> in Year field
    And I select <Country> in Country
    And I fill <cellphone> in Mobile phone field
    And I fill <current email> in Your current email address field
    And I click on "Sign Up" button
    Then I should see the message: Account created successfully

    Examples:
      | first name | last name | username      | password    | month     | day  | year     |  Country | cellphone | current email |
      |  Maria     | Vargas    | maria.vargas  | Control123* | July      | 1    | 1890     |Bolivia  | 77777777  | maria.vargas@gmail.com |
      |  Miguel    | Vargas    | miguel.vargas | Control123* | September | 30   | 1991     |Bolivia  | 77777777  | miguel@gmail.com |


  Scenario Outline: Creation of account Successful without filling Birthday section
    Given I am looking at the creation account page
    When I fill <first name> in first name field
    And I fill the <last name> in last name field
    And I fill the <username> in username
    And I fill the <password> in Create a password field
    And I select <gender> in Gender dropdown
    And I select <Country> in Country
    And I fill <cellphone> in Mobile phone field
    And I fill <current email> in Your current email address field
    And I click on "Sign Up" button
    Then I should see the message: Account created successfully

    Examples:
      | first name | last name | username      | password    |  gender |Country  | cellphone | current email|
      |  Maria     | Vargas    | maria.vargas  | Control123* | F       |Bolivia  | 77777777  | maria.vargas@gmail.com |
      |  Miguel    | Vargas    | miguel.vargas | Control123* | M       |Bolivia  | 77777777  | miguel@gmail.com |


  Scenario Outline: Creation of account Successful without filling Mobile phone
    Given I am looking at the creation account page
    When I fill <first name> in first name field
    And I fill the <last name> in last name field
    And I fill the <username> in username
    And I fill the <password> in Create a password field
    And I select <month> in Birthday dropdown
    And I fill <day> in Day field
    And I fill <year> in Year field
    And I select <gender> in Gender dropdown
    And I select <Country> in Country
    And I fill <current email> in Your current email address field
    And I click on "Sign Up" button
    Then I should see the message: Account created successfully

    Examples:
      | first name | last name | username | password | month | day | year | gender| Country | current email|
      |  Maria | Vargas | maria.vargas | Control123* | July | 1 | 2000 |    F  | Bolivia  | maria.vargas @gmail.com |
      |  Miguel | Vargas | miguel.vargas | Control123* | September | 30 | 1991 |  M  | Bolivia  | miguel@gmail.com |


  Scenario Outline: Creation of the account failed filling firs name or last name with numbers or special character
    Given I am looking at the creation account page
    When I fill <first name> in first name field
    And I fill the <last name> in last name field
    And I fill the <username> in username
    And  I fill the <password> in Create a password field
    Then I should see the message: The account can't be created
    Examples:
      | first name | last name | username | password |
      |  Marco     | P3r3z     | marco.p  | Control123* |
      |  Michael"s | P4rD()    | michaelp | Control123* |


  Scenario: Creation of the account failed when the user name  was registered
    Given I am looking at the creation account page
    When I fill Araceli in first name field
    And I fill the Pardo in last name field
    And I fill the araceli.p in username
    And  I fill the Control123* in Create a password field
    Then I should see the message: The account can't be created


  Scenario Outline: Creation of the account failed when the user name isn't valid
    Given I am looking at the creation account page
    When I fill <first name> in first name field
    And I fill the <last name> in last name field
    And I fill the <username> in username
    And  I fill the <password> in Create a password field
    Then I should see the message: The account can't be created
    Examples:
      | first name | last name | username | password |
      |  Marco     | Perez     | .marcop  | Control123* |
      |  Pedro     | Pardo     | pedro_p  | Control123* |
      |  Pedro     | Pardo     | 123pedro | Control123* |
      |  Pedro     | Pardo     |          | Control123* |


  Scenario Outline: Creation of the account failed when the password isn't valid
    Given I am looking at the creation account page
    When I fill <first name> in first name field
    And I fill the <last name> in last name field
    And I fill the <username> in username
    And  I fill the <password> in Create a password field
    Then I should see the message: The account can't be created
    Examples:
      | first name | last name | username | password |
      |  Marco     | Perez     | marcop.2 | 1234567  |
      |  Pedro     | Pardo     | pedro_p  | controlp |
      |  Pedro     | Vargas    | pedro_p  |          |


  Scenario Outline: Creation of the account failed when the password confirm invalid
    Given I am looking at the creation account page
    When I fill <first name> in first name field
    And I fill the <last name> in last name field
    And I fill the <username> in username
    And  I fill the <password> in Create a password field
    And  I fill the <password confirm> in Confirm your password field
    Then I should see the message: The account can't be created
    Examples:
      | first name | last name | username | password    | password confirm |
      |  Marco     | Perez     | marcop.2 | Control123* | control*   |
      |  Pedro     | Pardo     | pedro_p  | Control123* |            |


   Scenario Outline: Creation of the account failed when the the cellphone isn't valid
    Given I am looking at the creation account page
    When I fill <first name> in first name field
    And I fill the <last name> in last name field
    And I fill the <username> in username
    And I fill the <password> in Create a password field
    And I fill <cellphone> in Mobile phone field
    And I click on "Sign Up" button
    Then I should see the message: The account can't be created

    Examples:
      | first name | last name | username      | password    | cellphone |
      |  Maria     | Vargas    | maria.vargas  | Control123* | 7777777  |
      |  Miguel    | Vargas    | miguel.vargas | Control123* | 78q789e  |
