import sqlite3


class Helper:
    def __init__(self,path):
        self.db_path = path

    def connect(self):
        self._conn = sqlite3.connect(self.db_path)

    def execute(self,query):
        self._cursor = self._conn.execute(query)
        self._rv = self._cursor.fetchall()

    def getAt(self,position):
        return self._rv[position]

    def size(self):
        return len(self._rv)

    def close(self):
        self._conn.close()