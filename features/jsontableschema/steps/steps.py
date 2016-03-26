# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from behave import given, when, then
from jsontableschema import push_resource, pull_resource


@when('We push/pull resource from "{path}" to sql')
def step_when_push_pull_resource(context, path):
    print(context, path)

@then('No errors are occured')
def step_then_no_errors_are_occured(context):
    assert not context.failed
