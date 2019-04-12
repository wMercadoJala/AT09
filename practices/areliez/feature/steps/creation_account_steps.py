from behave import *

use_step_matcher("parse")


@then("I should see the error message: {error:w}")
def step_impl(context, error):
    """
    :type context: behave.runner.Context
    :type arg0: str
    """
    pass


use_step_matcher("re")


@given("I am looking at the creation account page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("*****Creation Page*****")


@when("I fill (([A-Za-z])\w+) in first name field")
def step_impl(context, first):
    """
    :type context: behave.runner.Context
    :type arg0: str
    """
    context.first = first


@step("I fill the (([A-Za-z])\w+) in last name field")
def step_impl(context, last):
    """
    :type context: behave.runner.Context
    :type arg0: str
    """
    context.last = last


@step("I fill the (.*) in username")
def step_impl(context, username):
    """
    :type context: behave.runner.Context
    :type username: str
    """
    context.username = username


@step("I fill the (^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$) in Create a password field")
def step_impl(context, password):
    """
    :type context: behave.runner.Context
    :type password: str
    """
    context.password = password


@step("I fill the (^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$) in Confirm your password field")
def step_impl(context, confirm_password):
    """
    :type context: behave.runner.Context
    :type arg0: str
    """
    context.confirm_password = confirm_password


@step("I fill (\d{1,2}) in Day field")
def step_impl(context, day):
    """
    :type context: behave.runner.Context
    :type day: str
    """
    context.day = day


@step("I fill (\d{4}) in Year field")
def step_impl(context, year):
    """
    :type context: behave.runner.Context
    :type year: str
    """
    context.year = year


@step("I select (^[FM]) in Gender dropdown")
def step_impl(context, gender):
    """
    :type context: behave.runner.Context
    :type gender: str
    """
    context.gender = gender


@step("I select (([A-Za-z])\w+) in Country")
def step_impl(context, Country):
    """
    :type context: behave.runner.Context
    :type Country: str
    """
    context.country = Country


@step(
    "I fill (^\s*(?:\+?(\d{1,3}))?([-. (]*(\d{3})[-. )]*)?((\d{3})[-. ]*(\d{2,4})(?:[-.x ]*(\d+))?)\s*$) in Mobile phone field")
def step_impl(context, cellphone):
    """
    :type context: behave.runner.Context
    :type cellphone: str
    """
    context.cellphone = cellphone


@step("I fill (.*) in Your current email address field")
def step_impl(context, email):
    """
    :type context: behave.runner.Context
    :type email: str
    """
    context.email = email


@step("I select (([A-Za-z])\w+) in Birthday dropdown")
def step_impl(context, month):
    """
    :type context: behave.runner.Context
    :type month: str
    """
    context.month = month


@then("I should have a message of successful")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step('I click on "Sign Up" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("click on button")
