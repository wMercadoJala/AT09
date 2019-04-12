from behave import *
from compare import *

from practices.raul.helpers.validator import Validator

use_step_matcher("re")

@given(u'we have a form to create a gmail account')
def step_impl(context):
    print("+=======================================================+")
    print("+=== You are into the form for create account gmail=====+")


@when("we fill the (.*) first name field")
def step_impl(context, first_name):
    """
    :type context: behave.runner.Context
    :type first_name: str
    """
    context.first_name = first_name


@when("we fill the (.*) last name field")
def step_impl(context, last_name):
    """
    :type context: behave.runner.Context
    :type last_name: str
    """
    context.last_name = last_name


@when(u'we fill the (.*) user name field')
def step_impl(context, user_name):
    context.user_name = user_name


@when(u'we fill the (.*) password field')
def step_impl(context, password):
    context.password = password


@when(u'we fill the  "confirm password" field')
def step_impl(context):
    context.confirm_password = context.password


@when(u'we press the "create" button for a new account')
def step_impl(context):

    context.result = Validator.validate_fields(context.first_name, context.last_name,
                                               context.user_name, context.password)
    # if context.first_name == '':
    #     context.result = 'Error!! the First Name is required'
    # elif context.last_name == '':
    #     context.result = 'Error!! the Last Name is required'
    # elif context.user_name == '':
    #     context.result = 'Error!! the User Name is required'
    # elif context.password == '':
    #     context.result = 'Error!! the Password is required'
    # elif context.confirm_password == '':
    #     context.result = 'Error!! the Confirm Password is required'
    # else:
    #     context.result = 'Congratulation!! Your account is successful'


@then(u'we have to a new gmail account with (.*)')
def step_impl(context, message):
    expect(context.result).to_equal(message)


@then(u'we have to go the Sign In page of gmail')
def step_impl(context):
    pass
