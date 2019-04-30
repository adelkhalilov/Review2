import flask
from flask import Flask
import psycopg2

app = Flask(__name__)


@app.route('/add_lesson', methods=['POST'])
def add_lesson():
    subject_name_ = flask.request.args['subject_name']
    day_of_the_week_ = flask.request.args['day_of_the_week']
    time_of_start_ = flask.request.args['time_of_start']
    params = dict(dbname="test", user="postgres", password="1234", host="localhost")
    with psycopg2.connect(**params) as conn:
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO timetable (subject_name, day_of_the_week, time_of_start) VALUES
                (%s, %s, %s)''', (str(subject_name_), str(day_of_the_week_), str(time_of_start_), ))
        conn.commit()
    return 'OK'


@app.route('/get_lessons', methods=['GET'])
def get_lessons():
    params = dict(dbname="test", user="postgres", password="1234", host="localhost")
    with psycopg2.connect(**params) as conn:
        cur = conn.cursor()
        cur.execute('''SELECT DISTINCT * FROM timetable''')
    a = cur.fetchall()
    ans = ""
    for y in a:
        for i in y:
            j = str(i)
            ans += j[0:len(j)]
            ans += ', '
        ans = ans[0: len(ans) - 2]
        ans += '\n'
    return ans


@app.route('/get_next_lesson', methods=['GET'])
def get_next_lesson():
    current_day = flask.request.args['current_day']
    current_time = flask.request.args['current_time']
    params = dict(dbname="test", user="postgres", password="1234", host="localhost")
    with psycopg2.connect(**params) as conn:
        cur = conn.cursor()
        cur.execute('''SELECT timetable.subject_name, timetable.day_of_the_week, MIN(timetable.time_of_start)
                FROM timetable
                WHERE timetable.day_of_the_week = %s AND timetable.time_of_start > %s
                GROUP BY timetable.subject_name, timetable.day_of_the_week''', (current_day, current_time))
    ans = ""
    for row in cur:
        subject_name, day_of_the_week, time_of_start = row
        ans += subject_name
        ans += ", "
        ans += day_of_the_week
        ans += ", "
        ans += str(time_of_start)
    if ans != "":
        return ans
    else:
        return "There are no more lessons today"



if __name__ == "__main__":
    PORT = '5000'
    app.run('127.0.0.1', PORT, debug=True, threaded=True)
