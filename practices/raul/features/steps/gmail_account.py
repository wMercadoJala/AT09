from behave import *


@given(u'we have a form to create a gmail account')
def step_impl(context):
    #raise NotImplementedError(u'STEP: Given we have a form to create a gmail account')
    pass


@then("we fill the {firstName} first name field")
def step_impl(context, firstName):
    """
    :type context: behave.runner.Context
    :type firstName: str
    """
    #raise NotImplementedError(u'STEP: Then we fill the <firstName> first name field')
    pass


@step("we fill the {lastName} last name field")
def step_impl(context, lastName):
    """
    :type context: behave.runner.Context
    :type lastName: str
    """
    #raise NotImplementedError(u'STEP: And we fill the <lastName> last name field')
    pass


@then(u'we fill the {userName} user name field')
def step_impl(context, userName):
    #raise NotImplementedError(u'STEP: Then we fill the <userName> user name field')
    pass


@then(u'we fill the {password} password field')
def step_impl(context, password):
    #raise NotImplementedError(u'STEP: Then we fill the <password> password field')
    pass

