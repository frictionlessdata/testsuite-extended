# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import sqlalchemy as sa
from behave import given, when, then
from jsontableschema import push_resource, pull_resource


@when('We push/pull resource from "{path}" to SQL')
def step_when_push_pull_resource(context, path):

    # Create engine
    engine = sa.create_engine('sqlite:///:memory:')

    # Push resource to storage
    push_resource(
        table='table',
        schema='%s/schema.json' % path,
        data='%s/data.csv' % path,
        backend='sql',
        engine=engine)

    # Pull resource from storage
    pull_resource(
        table='table',
        schema='target/%s/schema.json' % path,
        data='target/%s/data.csv' % path,
        backend='sql',
        engine=engine)


@then('No errors are occured')
def step_then_no_errors_are_occured(context):

    # Assertions
    assert not context.failed
