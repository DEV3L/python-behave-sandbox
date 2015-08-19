from behave import *


@given('we have behave installed')
def step_impl(context):
    print('in step: we have behave installed\n')
    pass


@when('we implement a test')
def step_impl(context):
    print('in step: we implement a test\n')
    assert True is not False


@then('behave will test it for us!')
def step_impl(context):
    print('in step: behave will test it for us!\n')
    assert context.failed is False
