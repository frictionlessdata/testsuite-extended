# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import io
import os
import json
import uuid
from behave import given, when, then
from apiclient.discovery import build
from oauth2client.client import GoogleCredentials
from datapackage import push_datapackage, pull_datapackage
from jsontableschema import push_resource, pull_resource
from jsontableschema.plugins.bigquery import Storage


# Prepare bigquery
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '.credentials.json'
credentials = GoogleCredentials.get_application_default()
service = build('bigquery', 'v2', credentials=credentials)
project = json.load(io.open('.credentials.json', encoding='utf-8'))['project_id']


@when('We push/pull resource from "{dataset}" to BigQuery')
def step_when_push_pull_resource_to_bigquery(context, dataset):

    # Generate prefix, set group
    prefix = '%s_' % uuid.uuid4().hex
    group = 'resource'

    try:

        # Push resource to storage
        push_resource(
            table='table',
            schema='datasets/%s/schema.json' % dataset,
            data='datasets/%s/data.csv' % dataset,
            backend='bigquery',
            service=service,
            project=project,
            dataset=group,
            prefix=prefix)

        # Pull resource from storage
        pull_resource(
            table='table',
            schema='target/bigquery/%s/schema.json' % dataset,
            data='target/bigquery/%s/data.csv' % dataset,
            backend='bigquery',
            service=service,
            project=project,
            dataset=group,
            prefix=prefix)

    finally:

        # Delete test tables from storage
        storage = Storage(service, project, group, prefix=prefix)
        storage.delete()


@when('We push/pull datapackage from "{dataset}" to BigQuery')
def step_when_push_pull_datapackage_to_bigquery(context, dataset):

    # Generate prefix, set group
    prefix = '%s_' % uuid.uuid4().hex
    group = 'datapackage'

    try:

        # Push datapackage to storage
        push_datapackage(
            descriptor='datasets/%s/datapackage.json' % dataset,
            backend='bigquery',
            service=service,
            project=project,
            dataset=group,
            prefix=prefix)

        # Pull datapackage from storage
        pull_datapackage(
            descriptor='target/bigquery/%s/datapackage.json' % dataset,
            name='name',
            backend='bigquery',
            service=service,
            project=project,
            dataset=group,
            prefix=prefix)

    finally:

        # Delete test tables from storage
        storage = Storage(service, project, group, prefix=prefix)
        storage.delete()
