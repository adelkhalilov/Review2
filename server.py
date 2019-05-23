import flask
from flask import Flask
import psycopg2
from config import params, PORT, numday
from datetime import datetime

app = Flask(__name__)


@app.route('/add_lesson', methods=['POST'])
def add_lesson():
    subject_name_ = flask.request.args['subject_name']
    day_of_the_week_ = flask.request.args['day_of_the_week']
    time_of_start_ = flask.request.args['time_of_start']
    time = datetime.strptime(time_of_start_, '%H:%M')
    id = int(time.strftime("%M")) + int(time.strftime("%H")) * 60 + numday[day_of_the_week_] * 24 * 60
    with psycopg2.connect(**params) as conn:
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO timetable (subject_name, day_of_the_week, time_of_start, id) VALUES
                (%s, %s, %s, %s)''', (str(subject_name_), str(day_of_the_week_), str(time_of_start_), id))
        conn.commit()
    return 'OK'


@app.route('/get_lessons', methods=['GET'])
def get_lessons():
    with psycopg2.connect(**params) as conn:
        cur = conn.cursor()
        cur.execute('''SELECT DISTINCT subject_name, day_of_the_week, time_of_start, id
                       FROM timetable
                       ORDER BY id''')
    a = cur.fetchall()
    ans = ""
    for y in a:
        for i in y:
            j = str(i)
            ans += j[0:len(j)]
            ans += ', '
        ans = ans[0: len(ans) - 2 - len(str(y[len(y) - 1])) - 2]
        ans += '\n'
    return ans


@app.route('/get_next_lesson', methods=['GET'])
def get_next_lesson():
    current_day = flask.request.args['current_day']
    current_time = flask.request.args['current_time']
    with psycopg2.connect(**params) as conn:
        cur = conn.cursor()
        cur.execute('''SELECT timetable.subject_name, timetable.day_of_the_week, MIN(timetable.time_of_start)
                FROM timetable
                WHERE timetable.day_of_the_week = %s AND timetable.time_of_start > %s
                GROUP BY timetable.subject_name, timetable.day_of_the_week, timetable.time_of_start
                ORDER BY timetable.time_of_start
                LIMIT(1)''', (current_day, current_time))
        ans = ""
        for row in cur:
            subject_name, day_of_the_week, time_of_start = row
            ans = ", ".join([subject_name, day_of_the_week, str(time_of_start)])
        if ans != "":
            return ans
        else:
            return "There are no more lessons today"




if __name__ == "__main__":
    app.run('127.0.0.1', PORT, debug=True, threaded=True)
