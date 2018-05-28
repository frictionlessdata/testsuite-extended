# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import io
import os
import json
import uuid
import pytest
from copy import deepcopy
from sqlalchemy import create_engine
from apiclient.discovery import build
from oauth2client.client import GoogleCredentials
from tableschema import Table, Storage, Schema


# Fixtures

GENERAL = {
    'schema': {
        'fields': [
            {'name': 'id', 'type': 'integer', 'constraints': {'required': True}},
            {'name': 'name', 'type': 'string'},
            {'name': 'current', 'type': 'boolean'},
            {'name': 'rating', 'type': 'number'},
            {'name': 'note', 'type': 'any'},
        ],
        'primaryKey': 'id',
    },
    'data': [
        ['id', 'name', 'current', 'rating', 'note'],
        ['1', 'Taxes', 'True', '9.5', 'note1'],
        ['2', '中国人', 'False', '7', 'note2'],
    ],
}
TEMPORAL = {
    'schema': {
        'fields': [
            {'name': 'date', 'type': 'date'},
            {'name': 'date_year', 'type': 'date', 'format': '%Y'},
            {'name': 'datetime', 'type': 'datetime'},
            {'name': 'duration', 'type': 'duration'},
            {'name': 'time', 'type': 'time'},
            {'name': 'year', 'type': 'year'},
            {'name': 'yearmonth', 'type': 'yearmonth'},
        ],
    },
    'data': [
        ['date', 'date_year', 'datetime', 'duration', 'time', 'year', 'yearmonth'],
        ['2015-01-01', '2015', '2015-01-01T03:00:00Z', 'P1Y1M', '03:00:00', '2015', '2015-01'],
        ['2015-12-31', '2015', '2015-12-31T15:45:33Z', 'P2Y2M', '15:45:33', '2015', '2015-01'],
    ],
}
LOCATION = {
    'schema': {
        'fields': [
            {'name': 'location', 'type': 'geojson'},
            {'name': 'geopoint', 'type': 'geopoint'},
        ],
    },
    'data': [
        ['location', 'geopoint'],
        ['{"type": "Point","coordinates":[33.33,33.33]}', '30,75'],
        ['{"type": "Point","coordinates":[50.00,50.00]}', '90,45'],
    ],
}
COMPOUND = {
    'schema': {
        'fields': [
            {'name': 'stats', 'type': 'object'},
            {'name': 'persons', 'type': 'array'},
        ],
    },
    'data': [
        ['stats', 'persons'],
        ['{"chars":560}', '["Mike", "John"]'],
        ['{"chars":970}', '["Paul", "Alex"]'],
    ],
}


# Tests

@pytest.mark.parametrize('name, resource', [
    ('general', GENERAL),
    ('temporal', TEMPORAL),
    ('location', LOCATION),
    ('compound', COMPOUND),
])
def test_table_bigquery(name, resource):

    # Storage
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '.credentials.json'
    credentials = GoogleCredentials.get_application_default()
    service = build('bigquery', 'v2', credentials=credentials)
    project = json.load(io.open('.credentials.json', encoding='utf-8'))['project_id']
    dataset = 'resource'
    prefix = '%s_' % uuid.uuid4().hex
    storage = Storage.connect('bigquery',
        service=service, project=project, dataset=dataset, prefix=prefix)

    # Save
    table = Table(resource['data'], schema=resource['schema'])
    table.save('table', storage=storage)

    # Load
    table = Table('table', schema=resource['schema'], storage=storage)
    assert table.read() == cast(resource)['data']

    # Clean
    storage.delete()


@pytest.mark.parametrize('name, resource', [
    #  ('general', GENERAL),
    ('temporal', TEMPORAL),
    ('location', LOCATION),
    ('compound', COMPOUND),
])
def test_table_pandas(name, resource):

    # Storage
    engine = create_engine('sqlite:///')
    storage = Storage.connect('pandas')

    # Save
    table = Table(resource['data'], schema=resource['schema'])
    table.save('table', storage=storage)

    # Load
    table = Table('table', schema=resource['schema'], storage=storage)
    assert table.read() == cast(resource)['data']


@pytest.mark.parametrize('name, resource', [
    ('general', GENERAL),
    ('temporal', TEMPORAL),
    ('location', LOCATION),
    ('compound', COMPOUND),
])
def test_table_sql(name, resource):

    # Storage
    engine = create_engine('sqlite:///')
    storage = Storage.connect('sql', engine=engine)

    # Save
    table = Table(resource['data'], schema=resource['schema'])
    table.save('table', storage=storage)

    # Load
    table = Table('table', schema=resource['schema'], storage=storage)
    assert table.read() == cast(resource)['data']


# Helpers

def cast(resource, skip=[]):
    resource = deepcopy(resource)
    schema = Schema(resource['schema'])
    resource['data'] = resource['data'][1:]
    for row in resource['data']:
        for index, field in enumerate(schema.fields):
            if field.type not in skip:
                row[index] = field.cast_value(row[index])
    return resource
