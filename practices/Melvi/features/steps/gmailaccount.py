from behave import given, when, then, use_step_matcher
from compare import *

from helpers.Validfields import Validfields


use_step_matcher("parse")

@given(u'Gmail page opened')
def step_impl(context):
    print("*********OPEN GMAIL REGISTRATION PAGE************")
    context.first = ''
    # context.last = ''
    context.user_name=''
    # context.pws = ''
    print (context.test)
@when(u'I fill first_name: {first}')
def step_impl(context, first):
    context.first = first


@when(u'I fill last_name: {last}')
def step_impl(context, last):
    context.last = last


@when(u'I fill user_name: {user_name}')
def step_impl(context, user_name):
    context.user_name= user_name

@when(u'I fill password: {pws}')
def step_impl(context, pws):
    context.pws = pws


@when(u'I fill confirm_pws')
def step_impl(context):
    context.confirm_pws = context.pws


@when(u'I fill birthday month: {month}')
def step_impl(context, month):
    context.month = month


@when(u'I fill birthday day: {day}')
def step_impl(context, day):
    context.day = day


@when(u'I fill birthday year: {year}')
def step_impl(context, year):
    context.year = year


@when(u'I fill gender: {gender}')
def step_impl(context, gender):
    context.gender = gender


@when(u'I fill country_code: {country_code}')
def step_impl(context, country_code):
    context.country_code = country_code


@when(u'I fill phone_number: {phone_number}')
def step_impl(context, phone_number):
    context.phone_number = phone_number


@when(u'I fill current_mail: {current_mail}')
def step_impl(context, current_mail):
    context.current_mail = current_mail


@when(u'I press the Register Button')
def step_impl(context):
   context.results = Validfields.perform_validated(context.first, context.last, context.user_name, context.pws,
                                                  context.month, context.day, context.year,
                                                  context.gender, context.country_code, context.phone_number,
                                                  context.current_mail)

@then(u'I get the {message} message')
def step_impl(context, message):
    expect(context.results).to_equal(message)

