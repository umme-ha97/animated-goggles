from behave import given, when, then
from features.pages.login_page import login_page
import configparser
import os

@given(u'User opens the url for the website')
def step_impl(context):
    context.page = login_page(context)
    context.page.open_url()

@then(u'User is on sign in page')
def step_impl(context):
    context.page = login_page(context)
    context.page.validate_page()

@then(u'User enters "{web_name}" name')
def step_impl(context, web_name):
    context.page = login_page(context)
    context.page.enter_name(web_name)

@then(u'User enters email as "{email}" email')
def step_impl(context,email):
    context.page = login_page(context)
    context.page.enter_email(email)

@then(u'User enters "{company_name}" company')
def step_impl(context,company_name):
    context.page = login_page(context)
    context.page.enter_company(company_name)

@then(u'User enters "{job}" as job title')
def step_impl(context, job):
    context.page = login_page(context)
    context.page.enter_job(job)

@then(u'User selects "{country_name}" for country code')
def step_impl(context, country_name):
    context.page = login_page(context)
    context.page.select_country(country_name)

@then(u'User enters "{phn_num}" phone number')
def step_impl(context, phn_num):
    context.page = login_page(context)
    context.page.enter_phn_number(phn_num)

@then(u'User selects the service from the dropdown')
def step_impl(context):
    context.page = login_page(context)
    context.page.select_service()

@then(u'User clicks on submit button')
def step_impl(context):
    context.page = login_page(context)
    context.page.click_btn()


