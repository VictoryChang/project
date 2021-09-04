from typing import List

from pypika import Query, Table, Field, Order


class SQLiteAdapter:
    def __init__(self, table: str):
        self.table = table

    def select(self, fields: List[str], sort_by: str = 'user_id', order: str = Order.asc):
        return str(Query.from_(self.table).select(*fields).orderby(sort_by, order=order))

    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

