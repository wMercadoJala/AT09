from behave import *
from compare import *
from helpers.Datos import Datos

use_step_matcher("re")

@given('I open the form for create gmail account')
def step_impl(context):
    print("-------------------------")
    print("***form create account***")
    print("-------------------------")

@when("I get form create account")
def step_impl(context):
    pass


@then("I receive status code 200")
def step_impl(context):
    pass

@when("I fill (.*) in First Name field")
def step_impl(context, first):
    context.first = first


@step("I fill (.*) in Last Name field")
def step_impl(context, last):
    context.last = last


@step("I fill (.*) in User Name field")
def step_impl(context, user_name):
    context.user_name = user_name


@step("I fill (.*) in Pass field")
def step_impl(context, password):
    context.password = password


@step("I fill confirm _pass in Confirm Pass field")
def step_impl(context):
    context.confirm_pass = context.password


@step("I fill (.*) in month Birthday field")
def step_impl(context, month):
    context.month = month


@step("I fill (\d{2,}) in day Birthday field")
def step_impl(context, day):
    context.day = day


@step("I fill (\d{2,}) in year Birthday field")
def step_impl(context, year):
    context.year = year


@step("I fill (.*) in Gender field")
def step_impl(context, gender):
    context.gender = gender


@step("I fill (.*) in Code field")
def step_impl(context, code):
    context.code = code


@step("I fill (.*) in mobile phone field")
def step_impl(context, phone):
    context.phone = phone


@step("I fill (.*) in Current Email field")
def step_impl(context, current_email):
    context.current_email = current_email


@when("I press next button")
def step_impl(context):
    context.result = Datos.required_data(context.first, context.last, context.user_name, context.password)


@then("(.*) created account")
def step_impl(context, result):
    expect(context.result).to_equal(result)


@then("I should have (.*)")
def step_impl(context, message):
    expect(context.result).to_equal(message)
