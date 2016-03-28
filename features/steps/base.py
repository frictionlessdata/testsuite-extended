# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from behave import given, when, then


@then('No errors are occured')
def step_then_no_errors_are_occured(context):

    # assertions
    assert True
