import pytest

from adapters.sqlite_adapter import SQLiteAdapter


@pytest.fixture()
def adapter():
    return SQLiteAdapter(table='table_name')


def test_select_field(adapter):
    sql = adapter.select(fields=['field'])
    assert sql == 'SELECT "field" FROM "table_name" ORDER BY "user_id" ASC'


def test_select_fields(adapter):
    sql = adapter.select(fields=['field1', 'field2'])
    assert sql == 'SELECT "field1","field2" FROM "table_name" ORDER BY "user_id" ASC'
