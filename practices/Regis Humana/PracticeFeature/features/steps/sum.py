from behave import *
from compare import *

from lib_help.Help import Operators


@given("I have the calculator open")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when(u'I put first number: {first:d}')
def step_impl(context, first):
    """
    :type context: behave.runner.Context
    """
    context.first = first


@step(u'I press {operator} button')
def step_impl(context, operator):
    """
    :type context: behave.runner.Context
    """
    context.operator = operator


@step("I put second number: {second:d}")
def step_impl(context, second):
    """
    :type context: behave.runner.Context
    """
    context.second = second


@step("I press = button to perform the operation")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.result = Operators.operators(context.first, context.second, context.operator)


@then("I should have {result:d} as a sum")
def step_impl(context, result):
    """
    :type context: behave.runner.Context
    """
    expect(context.result).to_equal(result)


@then("I should have {message}")
def step_impl(context, message):
    """
    :type context: behave.runner.Context
    """
    expect(context.result).to_equal(message)


@when("I will perform the operation {first} {operator} {second}")
def step_impl(context, first, operator, second):
    """
    :type context: behave.runner.Context
    """
    context.execute_steps('''
    When I put first number: %s
    And I press %s button
    And I put second number: %s
    And I press = button to perform the operation
    ''' % (first, operator, second))

