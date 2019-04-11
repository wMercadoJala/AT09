Feature: Test the form to create a new gmail account

  Scenario Outline: Create a new gmail account
    Given we have a form to create a gmail account
     Then we fill the <firstName> first name field
      And we fill the <lastName> last name field
      And we fill the <userName> user name field
      And we fill the <password> password field
  Examples: fields
    |firstName|lastName|userName|password|
    |Raul     |Choque  |raulito |!r000:) |