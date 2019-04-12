from behave import *
from compare import *


@given(u'we have a form to create a gmail account')
def step_impl(context):
    print("+=======================================================+")
    print("+=== You are into the form for create account gmail=====+")


@when("we fill the {first_name} first name field")
def step_impl(context, first_name):
    """
    :type context: behave.runner.Context
    :type first_name: str
    """
    context.first_name = first_name


@when("we fill the {last_name} last name field")
def step_impl(context, last_name):
    """
    :type context: behave.runner.Context
    :type last_name: str
    """
    context.last_name = last_name


@when(u'we fill the {user_name} user name field')
def step_impl(context, user_name):
    context.user_name = user_name


@when(u'we fill the {password} password field')
def step_impl(context, password):
    context.password = password

@when(u'we fill the  "confirm password" field')
def step_impl(context):
    context.confirm_password = context.password


@when(u'we press the "create" button for a new account')
def step_impl(context):
    pass


@then(u'we have to a new gmail account with {message_successful}')
def step_impl(context, message_successful):
    expect(get_message_successful()).to_equal(message_successful)


@then(u'we have to go the Sign In page of gmail')
def step_impl(context):
    pass


def get_message_successful():
    return "Congratulation!! Your account is successful"

