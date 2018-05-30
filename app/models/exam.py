from app.utils.dbutil import dbutil
import sqlite3

class exam(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def getAllRecord():
        db = dbutil()
        db.execute('select id,question,answer from examresult')
        ret = db.fetchall()
        list = []
        listkey = ['key','chinese', 'english']
        for item in ret:
            list.append(dict(zip(listkey, item)))
        return list

    @staticmethod
    def generateResult(data):
        db = dbutil()
        keys = data.keys()
        values = data.values()
        params = list(zip(values, values, keys))
        print(params)
        db.executemany('''update examresult 
                          set reply=?, examtimes= examtimes+1,
                          errortimes=case when answer!=reply then errortimes+1 end,
                          isok=case when trim(answer)=trim(?) then 1 else 0 end  
                          where id=?''', params)
        ret = db.commit()

    @staticmethod
    def getExamResult():
        db = dbutil()
        db.execute('select id,question,answer, reply, isok from examresult')
        ret = db.fetchall()
        list = []
        listkey = ['id', 'question', 'answer', 'reply', 'isok']
        for item in ret:
            list.append(dict(zip(listkey, item)))
        return list

# print(exam.getAllRecord())
# print(exam.getExamResult())