from behave import *

use_step_matcher("re")


@given("I am looking at the creation account page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    #raise NotImplementedError(u'STEP: Given I am looking at the creation account page')
    pass


@given("I fill (.+) in first name field")
def step_impl(context, arg0):
    """
    :type context: behave.runner.Context
    :type arg0: str
    """
    raise NotImplementedError(u'STEP: Given I fill <first name> in first name field')


@step("I fill the (.+) in last name field")
def step_impl(context, arg0):
    """
    :type context: behave.runner.Context
    :type arg0: str
    """
    raise NotImplementedError(u'STEP: And I fill the <last name> in last name field')


@given("I open the browser at : www\.gmail\.com/singup")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given I open the browser at : www.gmail.com/singup')


@step("I fill the (?P<username>.+) in username")
def step_impl(context, username):
    """
    :type context: behave.runner.Context
    :type username: str
    """
    raise NotImplementedError(u'STEP: And I fill the <username> in username')


@step("I fill the (?P<password>.+) in Create a password field")
def step_impl(context, password):
    """
    :type context: behave.runner.Context
    :type password: str
    """
    raise NotImplementedError(u'STEP: And  I fill the <password> in Create a password field')


@step("I fill (?P<day>.+) in Day field")
def step_impl(context, day):
    """
    :type context: behave.runner.Context
    :type day: str
    """
    raise NotImplementedError(u'STEP: And I fill <day> in Day field')


@step("I fill (?P<year>.+) in Year field")
def step_impl(context, year):
    """
    :type context: behave.runner.Context
    :type year: str
    """
    raise NotImplementedError(u'STEP: And I fill <year> in Year field')


@step("I select (?P<gender>.+) in Gender dropdown")
def step_impl(context, gender):
    """
    :type context: behave.runner.Context
    :type gender: str
    """
    raise NotImplementedError(u'STEP: And I select <gender> in Gender dropdown')


@step("I select (?P<Country>.+) in Country")
def step_impl(context, Country):
    """
    :type context: behave.runner.Context
    :type Country: str
    """
    raise NotImplementedError(u'STEP: And I select <Country> in Country')


@step("I fill (?P<cellphone>.+) in Mobile phone field")
def step_impl(context, cellphone):
    """
    :type context: behave.runner.Context
    :type cellphone: str
    """
    raise NotImplementedError(u'STEP: And I fill <cellphone> in Mobile phone field')


@step("I fill (.+) in Your current email address field")
def step_impl(context, arg0):
    """
    :type context: behave.runner.Context
    :type arg0: str
    """
    raise NotImplementedError(u'STEP: And I fill <current email> in Your current email address field')


@step("I select (?P<month>.+) in Birthday dropdown")
def step_impl(context, month):
    """
    :type context: behave.runner.Context
    :type month: str
    """
    raise NotImplementedError(u'STEP: And I select <month> in Birthday dropdown')
