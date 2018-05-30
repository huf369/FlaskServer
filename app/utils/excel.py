import xlrd
from utils.dbutil import dbutil

db = dbutil()
data = xlrd.open_workbook('/Users/teagreen/Downloads/grade3.xlsx')
table = data.sheet_by_index(0)
rows = table.nrows
for i in range(rows):
    detail = table.row_values(i)
    print(detail)
    print('insert into bookdetail VALUES (1,?,1,?,?,?)',(int(detail[0]),int(detail[1]),detail[2],detail[5]))
    db.execute('insert into bookdetail VALUES (1,?,1,?,?,?)',(int(detail[0]),int(detail[1]),detail[2],detail[5]))
db.commit()
