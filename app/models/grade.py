from app.utils.dbutil import dbutil
import sqlite3

class grade(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def getAllRecord():
        db = dbutil()
        db.execute('select * from grade')
        ret = db.fetchall()
        list = []
        listkey = ['name', 'value', 'checked']
        for item in ret:
            list.append(dict(zip(listkey, item)))
        return list

grade.getAllRecord()
