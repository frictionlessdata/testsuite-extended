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
from tableschema import Storage
from datapackage import Package
from sqlalchemy import create_engine
from apiclient.discovery import build
from oauth2client.client import GoogleCredentials


# Fixtures

PACKAGES = [
    'country-codes',
    'country-list',
    'currency-codes',
    's-and-p-500-companies',
    's-and-p-500',
]


# Tests

@pytest.mark.parametrize('name', PACKAGES)
def test_table_bigquery(name):

    # Storage
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '.credentials.json'
    credentials = GoogleCredentials.get_application_default()
    service = build('bigquery', 'v2', credentials=credentials)
    project = json.load(io.open('.credentials.json', encoding='utf-8'))['project_id']
    dataset = 'package'
    prefix = '%s_' % uuid.uuid4().hex
    storage = Storage.connect('bigquery',
        service=service, project=project, dataset=dataset, prefix=prefix)

    # Save
    package = Package('data/packages/%s/datapackage.json' % name)
    package.save(storage=storage)

    # Load
    package = Package(storage=storage)
    assert package.resources
    for resource in package.resources:
        assert resource.read()

    # Clean
    storage.delete()


@pytest.mark.parametrize('name', PACKAGES)
def test_table_pandas(name):

    # Storage
    storage = Storage.connect('pandas')

    # Save
    package = Package('data/packages/%s/datapackage.json' % name)
    package.save(storage=storage)

    # Load
    package = Package(storage=storage)
    assert package.resources
    for resource in package.resources:
        assert resource.read()


@pytest.mark.parametrize('name', PACKAGES)
def test_table_sql(name):

    # Storage
    engine = create_engine('sqlite:///')
    storage = Storage.connect('sql', engine=engine)

    # Save
    package = Package('data/packages/%s/datapackage.json' % name)
    package.save(storage=storage)

    # Load
    package = Package(storage=storage)
    assert package.resources
    for resource in package.resources:
        assert resource.read()
