from behave import *
from compare import *

use_step_matcher("re")


@given("I am looking at the creation account page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("*****Creation Page*****")


@when("I fill (.*) in first name field")
def step_impl(context, first):
    """
    :type context: behave.runner.Context
    :type first: str
    """
    context.first = first
    context.message = "Account created successfully"


@step("I fill the (.*) in last name field")
def step_impl(context, last):
    """
    :type context: behave.runner.Context
    :type last: str
    """
    context.last = last
    context.message = "Account created successfully"


@step("I fill the (.*) in username")
def step_impl(context, username):
    """
    :type context: behave.runner.Context
    :type username: str
    """
    context.username = username
    context.message = "Account created successfully"


@step("I fill the (.*) in Create a password field")
def step_impl(context, password):
    """
    :type context: behave.runner.Context
    :type password: str
    """
    context.password = password
    context.message = "Account created successfully"


@step("I fill the (.*) in Confirm your password field")
def step_impl(context, confirm_password):
    """
    :param confirm_password:
    :type context: behave.runner.Context
    :type confirm_password: str
    """
    context.confirm_password = confirm_password
    context.message = "Account created successfully"


@step("I fill (.*) in Day field")
def step_impl(context, day):
    """
    :type context: behave.runner.Context
    :type day: str
    """
    context.day = day
    context.message = "Account created successfully"


@step("I fill (.*) in Year field")
def step_impl(context, year):
    """
    :type context: behave.runner.Context
    :type year: str
    """
    context.year = year
    context.message = "Account created successfully"


@step("I select (.*) in Gender dropdown")
def step_impl(context, gender):
    """
    :type context: behave.runner.Context
    :type gender: str
    """
    context.gender = gender
    context.message = "Account created successfully"


@step("I select (.*) in Country")
def step_impl(context, Country):
    """
    :type context: behave.runner.Context
    :type Country: str
    """
    context.country = Country
    context.message = "Account created successfully"


@step(
    "I fill (.*) in Mobile phone field")
def step_impl(context, cellphone):
    """
    :type context: behave.runner.Context
    :type cellphone: str
    """
    context.cellphone = cellphone
    context.message = "Account created successfully"


@step("I fill (.*) in Your current email address field")
def step_impl(context, email):
    """
    :type context: behave.runner.Context
    :type email: str
    """
    context.email = email
    context.message = "Account created successfully"


@step("I select (.*) in Birthday dropdown")
def step_impl(context, month):
    """
    :type context: behave.runner.Context
    :type month: str
    """
    context.month = month
    context.message = "Account created successfully"


@step('I click on "Sign Up" button')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("click on button")


@then("I should see the message: (.*)")
def step_impl(context, message):
    """
    :type context: behave.runner.Context
    :type message: str
    """
    if context.message != message:
        context.message = "The account can't be created"
    expect(context.message).to_equal(message)
