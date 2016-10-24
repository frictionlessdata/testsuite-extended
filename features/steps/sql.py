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


# Prepare sql
engine = sa.create_engine('sqlite:///:memory:')


@when('We push/pull resource from "{dataset}" to SQL')
def step_when_push_pull_resource_to_sql(context, dataset):

    # Generate prefix
    prefix = '%s_' % uuid.uuid4().hex

    try:

        # Push resource to storage
        push_resource(
            table='table',
            schema='datasets/%s/schema.json' % dataset,
            data='datasets/%s/data.csv' % dataset,
            backend='sql',
            engine=engine,
            prefix=prefix)

        # Pull resource from storage
        pull_resource(
            table='table',
            schema='target/sql/%s/schema.json' % dataset,
            data='target/sql/%s/data.csv' % dataset,
            backend='sql',
            engine=engine,
            prefix=prefix)

    finally:

        # Delete test tables from storage
        storage = Storage(engine, prefix=prefix)
        storage.delete()


@when('We push/pull datapackage from "{dataset}" to SQL')
def step_when_push_pull_datapackage_to_sql(context, dataset):

    # Generate prefix
    prefix = '%s_' % uuid.uuid4().hex

    try:

        # Push datapackage to storage
        push_datapackage(
            descriptor='datasets/%s/datapackage.json' % dataset,
            backend='sql',
            engine=engine,
            prefix=prefix)

        # Pull datapackage from storage
        pull_datapackage(
            descriptor='target/sql/%s/datapackage.json' % dataset,
            name='name',
            backend='sql',
            engine=engine,
            prefix=prefix)

    finally:

        # Delete test tables from storage
        storage = Storage(engine, prefix=prefix)
        storage.delete()
