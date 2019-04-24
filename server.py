import flask
from flask import Flask
from flask import request
import requests

app = Flask(__name__)


@app.route('/add_lesson', methods=['POST'])
def add_lesson():
    subject_name = flask.request.args['subject_name']
    day_of_the_week = flask.request.args['day_of_the_week']
    time_of_start = flask.request.args['time_of_start']
    return ('OK')

@app.route('/get_lessons', methods=['POST'])
def get_lessons():
    return ('Timetable will be here')

if __name__ == "__main__":
    PORT = '5000'
    app.run('127.0.0.1', PORT, debug=True, threaded=True)
