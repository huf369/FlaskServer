from app.utils.dbutil import dbutil
import sqlite3

class course(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def getAllRecord(self):
        db = dbutil()
        db.execute('select * from course')
        values = dict(db.fetchall())
        print(values)
        db.close()
