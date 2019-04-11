Feature: Create new account of gmail
  As a common user
  I want to create a new account
  In order to verify the creation of  an account successful

  Scenario: Successful creation account
    Given I open the browser at : www.gmail.com/singup

  Scenario Outline: Successful creation account sending only required fields
    Given I am looking at the creation account page
    Given I fill <first name> in first name field
    And I fill the <last name> in last name field
    And I fill the <username> in username
    And  I fill the <password> in Create a password field

    Examples:
      | first name | last name | username | password |
      |  Areliez | Vargas | areliez.vargas | Control123* |
      |  Areliez | Vargas | areliez.123 | Control123* |
      |  Areliez | Vargas | Are456 | Control123* |
      |  Areliez | Vargas | areliez.vargas.123 | Control123* |
      |  Areliez | Vargas | areliez| Control123* |
      |  Areliez | Vargas | areliez.vargas | Control8 |

  Scenario Outline: Successful creation account all fields
    Given I am looking at the creation account page
    Given I fill <first name> in first name field
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

    Examples:
      | first name | last name | username | password | month | day | year | gender| Country | cellphone | current email|
      |  Areliez | Vargas | areliez.vargas | Control123* | July | 1 | 2000 |    F  | Bolivia | 77777777 | areliez.vargas@gmail.com |
      |  Areliez | Vargas | areliez.123 | Control123* | July | 1 | 2000 |    F  | Bolivia | 77777777 | areliez.vargas@gmail.com |
      |  Miguel | Vargas | miguel | Control123* | July | 1 | 1991 |  M  | Bolivia | 77777777 | miguel@gmail.com |


  Scenario Outline: Successful creation account all fields without send the year and gender
    Given I am looking at the creation account page
    Given I fill <first name> in first name field
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

   Examples:
      | first name | last name | username | password | month | day  |  Country | cellphone | current email|
      |  Areliez | Vargas | areliez.vargas | Control123* | July | 1 |        |           |              |
      |  Areliez | Vargas | areliez.123 | Control123* | |        |         |           |              |
      |  Areliez | Vargas | Are456 | Control123* | |        |         |           |              |
      |  Areliez | Vargas | areliez.vargas.123 | Control123* |  |       |         |           |              |
      |  Areliez | Vargas | areliez| Control123* | |          |         |           |              |
      |  Areliez | Vargas | areliez.vargas | Control8 |     |       |         |           |              |


  Scenario Outline: Successful creation account without Birthday section
    Given I am looking at the creation account page
    Given I fill <first name> in first name field
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

   Examples:
      | first name | last name | username | password |  |  Country | cellphone | current email|
      |  Areliez | Vargas | areliez.vargas | Control123* ||      |           |              |
      |  Areliez | Vargas | areliez.123 | Control123*    ||        |           |              |
      |  Areliez | Vargas | Are456 | Control123* |        |         |           |              |
      |  Areliez | Vargas | areliez.vargas.123 | Control123* |       |         |           |              |
      |  Areliez | Vargas | areliez| Control123* | |                  |           |              |
      |  Areliez | Vargas | areliez.vargas | Control8 |           |         |           |              |
