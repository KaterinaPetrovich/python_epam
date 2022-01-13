import sqlite3


class TableData:
    def __init__(self, database_name, table_name):
        if not table_name.isalnum:
            raise ValueError
        self.database = database_name
        self.table = table_name

    def __len__(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT COUNT(*) FROM {self.table}")
            return cursor.fetchone()[0]

    def __contains__(self, item):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT * FROM {self.table} WHERE name=:name", {"name": item}
            )
            return bool(cursor.fetchall())

    def __iter__(self):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {self.table}")
            while row := cursor.fetchone():
                yield row

    def __getitem__(self, key):
        with sqlite3.connect(self.database) as conn:
            cursor = conn.cursor()
            cursor.execute(
                f"SELECT * FROM {self.table} WHERE name=:name", {"name": key}
            )
            return cursor.fetchall()
