# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import uuid
import sqlalchemy as sa
from behave import given, when, then
from jsontableschema import push_resource, pull_resource
from jsontableschema.plugins.sql import Storage

# Prepare sql
engine = sa.create_engine('sqlite:///:memory:')


@when('We push/pull resource from "{path}" to SQL')
def step_when_push_pull_resource_to_sql(context, path):

    # Generate prefix
    prefix = '%s_' % uuid.uuid4().hex

    try:

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
            schema='target/sql/%s/schema.json' % path,
            data='target/sql/%s/data.csv' % path,
            backend='sql',
            engine=engine)

    finally:

        # Delete test tables from storage
        storage = Storage(engine, prefix=prefix)
        for table in storage.tables:
            storage.delete(table)
