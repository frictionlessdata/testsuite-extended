from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from functools import partial
from goodtables import validate


# Tests

def test_goodtables():
    source = 'https://raw.githubusercontent.com/frictionlessdata/goodtables-py/master/data/datapackages/invalid/%s'
    report = validate(source % 'datapackage.json')
    report = remove_keys(report, keys=['time'])
    assert report == {
        'valid': False,
        'table-count': 2,
        'warnings': [],
        'error-count': 2,
        'preset': 'datapackage',
        'tables': [
            {
                'headers': ['id', 'name', 'description', 'amount'],
                'datapackage': source % 'datapackage.json',
                'errors': [
                    {
                        'column-number': None,
                        'row-number': 3,
                        'row': [],
                        'code': 'blank-row',
                        'message': 'Row 3 is completely blank'
                    }
                ],
                'schema': 'table-schema',
                'row-count': 4,
                'valid': False,
                'error-count': 1,
                'scheme': None,
                'encoding': None,
                'format': 'inline',
                'source': source % 'data.csv',
            },
            {
                'headers': ['parent', 'comment'],
                'datapackage': source % 'datapackage.json',
                'errors': [
                    {
                        'column-number': None,
                        'row-number': 4,
                        'row': [],
                        'code': 'blank-row',
                        'message': 'Row 4 is completely blank'
                    }
                ],
                'schema': 'table-schema',
                'row-count': 5,
                'valid': False,
                'error-count': 1,
                'scheme': None,
                'encoding': None,
                'format': 'inline',
                'source': source % 'data2.csv',
            }
        ]
    }


# Helpers

def remove_keys(value, keys=[]):
    if isinstance(value, dict):
        for item_key, item_value in list(value.items()):
            if item_key in keys:
                del value[item_key]
                continue
            if isinstance(item_value, list):
                value[item_key] = list(map(partial(remove_keys, keys=keys), item_value))
    return value
