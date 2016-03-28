# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import uuid
import sqlalchemy as sa
from behave import given, when, then
from datapackage import push_datapackage, pull_datapackage
from jsontableschema import push_resource, pull_resource
from jsontableschema.plugins.sql import Storage


@when('We push/pull resource from "{path}" to SQL')
def step_when_push_pull_resource_to_sql(context, path):

    # Prepare sql
    # TODO: move to module-level:
    # https://github.com/frictionlessdata/jsontableschema-sql-py/issues/21
    engine = sa.create_engine('sqlite:///:memory:')

    # Generate prefix
    prefix = '%s_' % uuid.uuid4().hex

    try:

        # Push resource to storage
        push_resource(
            table='table',
            schema='%s/schema.json' % path,
            data='%s/data.csv' % path,
            backend='sql',
            engine=engine,
            prefix=prefix)

        # Pull resource from storage
        pull_resource(
            table='table',
            schema='target/sql/%s/schema.json' % path,
            data='target/sql/%s/data.csv' % path,
            backend='sql',
            engine=engine,
            prefix=prefix)

    finally:

        # Delete test tables from storage
        storage = Storage(engine, prefix=prefix)
        for table in storage.tables:
            # TODO: remove try-except
            # https://github.com/frictionlessdata/jsontableschema-sql-py/issues/21
            try:
                storage.delete(table)
            except Exception:
                pass


@when('We push/pull datapackage from "{path}" to SQL')
def step_when_push_pull_datapackage_to_sql(context, path):

    # Prepare sql
    # TODO: move to module-level:
    # https://github.com/frictionlessdata/jsontableschema-sql-py/issues/21
    engine = sa.create_engine('sqlite:///:memory:')

    # Generate prefix
    prefix = '%s_' % uuid.uuid4().hex

    try:

        # Push datapackage to storage
        push_datapackage(
            descriptor='%s/datapackage.json' % path,
            backend='sql',
            engine=engine,
            prefix=prefix)

        # Pull datapackage from storage
        pull_datapackage(
            descriptor='target/sql/%s/datapackage.json' % path,
            name='name',
            backend='sql',
            engine=engine,
            prefix=prefix)

    finally:

        # Delete test tables from storage
        storage = Storage(engine, prefix=prefix)
        for table in storage.tables:
            # TODO: remove try-except
            # https://github.com/frictionlessdata/jsontableschema-sql-py/issues/21
            try:
                storage.delete(table)
            except Exception:
                pass