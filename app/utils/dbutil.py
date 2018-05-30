import sqlite3

class dbutil(object):

    def __init__(self):
        self.conn = sqlite3.connect('/Users/teagreen/PycharmProjects/FlaskServer/app/database/education.db')
        self.cursor = self.conn.cursor();

    def execute(self, sqlScript, paramters=[]):
        self.cursor.execute(sqlScript, paramters)

    def executemany(self, sqlScript, paramters=[]):
        self.cursor.executemany(sqlScript, paramters)

    def fetone(self):
        self.cursor.fetchone();

    def fetchall(self):
        return self.cursor.fetchall();

    def commit(self):
        self.conn.commit();

    def close(self):
        self.cursor.close()
        self.conn.close()
