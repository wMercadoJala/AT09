Feature: Test the form to create a new gmail account

  Scenario Outline: Create a new gmail account
    Given we have a form to create a gmail account
     When we fill the <first_name> first name field
      And we fill the <last_name> last name field
      And we fill the <user_name> user name field
      And we fill the <password> password field
      And we fill the  "confirm password" field
      And we press the "create" button for a new account
     Then we have to a new gmail account with <message_successful>
      And we have to go the Sign In page of gmail
  Examples: fields
    |first_name|last_name|user_name|password|message_successful|
    |Raul     |Choque  |raulito |!r000:) |Congratulation!! Your account is successful|