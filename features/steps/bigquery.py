# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

import io
import os
import json
from behave import given, when, then
from apiclient.discovery import build
from oauth2client.client import GoogleCredentials
from jsontableschema import push_resource, pull_resource


@when('We push/pull resource from "{path}" to BigQuery')
def step_when_push_pull_resource_to_bigquery(context, path):

    # Prepare bigquery
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '.credentials.json'
    credentials = GoogleCredentials.get_application_default()
    service = build('bigquery', 'v2', credentials=credentials)
    project = json.load(io.open('.credentials.json', encoding='utf-8'))['project_id']

    # Push resource to storage
    push_resource(
        table='testing',
        schema='%s/schema.json' % path,
        data='%s/data.csv' % path,
        backend='bigquery',
        service=service,
        project=project,
        dataset='jsontableschema')

    # Pull resource from storage
    pull_resource(
        table='testing',
        schema='target/bigquery/%s/schema.json' % path,
        data='target/bigquery/%s/data.csv' % path,
        backend='bigquery',
        service=service,
        project=project,
        dataset='jsontableschema')
