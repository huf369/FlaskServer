from flask import Flask, request
from app.models.grade import grade
from app.models.exam import exam
from app.utils.strutil import strutil
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/exam', methods=['GET', 'POST'])
def ExamHandler():
    if request.method == 'POST':
        if strutil.is_json(request.data):
            data = json.loads(request.data)
            exam.generateResult(data)
            return ''
    else:
        if strutil.is_json(request.data):
            data = json.loads(request.data)
            print(data)
        values = exam.getAllRecord()
        return json.dumps(values,ensure_ascii=False)

@app.route('/examresult', methods=['GET'])
def ExamResultHandler():
    if request.method == 'GET':
        values = exam.getExamResult()
        return json.dumps(values,ensure_ascii=False)

@app.route('/courses', methods=['GET'])
def GetCourseHandler():
    if request.method == 'GET':
        values = grade.getAllRecord()
        return json.dumps(values,ensure_ascii=False)

@app.route('/grades' , methods=['GET'])
def GetGradeHandler():
    if request.method == 'GET':
        values = grade.getAllRecord()
        return json.dumps(values,ensure_ascii=False)


if __name__ == '__main__':
    app.debug = True
    app.run()
