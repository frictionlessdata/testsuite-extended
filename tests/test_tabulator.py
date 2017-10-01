from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from tabulator import Stream


# Fixtures

DATA = [
    {'id': 'en', 'name': 'english'},
    {'id': 'ch', 'name': '中国人'},
]

# Tests

def test_tabulator_csv():
    with Stream('data/resources/table.csv', headers=1) as stream:
        assert stream.read(keyed=True) == DATA


def test_tabulator_json():
    with Stream('data/resources/table.json', headers=1) as stream:
        assert stream.read(keyed=True) == DATA


def test_tabulator_ndjson():
    with Stream('data/resources/table.ndjson', headers=1) as stream:
        assert stream.read(keyed=True) == DATA


def test_tabulator_ods():
    with Stream('data/resources/table.ods', headers=1) as stream:
        assert stream.read(keyed=True) == DATA


def test_tabulator_tsv():
    with Stream('data/resources/table.tsv', headers=1) as stream:
        assert stream.read(keyed=True) == DATA


def test_tabulator_xls():
    with Stream('data/resources/table.xls', headers=1) as stream:
        assert stream.read(keyed=True) == DATA


def test_tabulator_xlsx():
    with Stream('data/resources/table.xlsx', headers=1) as stream:
        assert stream.read(keyed=True) == DATA
