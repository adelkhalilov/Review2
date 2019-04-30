# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
import psycopg2


params = dict(dbname="test", user="postgres", password="1234", host="localhost")

with psycopg2.connect(**params) as conn:
    cur = conn.cursor()
    # Удалим старые таблицы, если есть.
    cur.execute('DROP TABLE IF EXISTS timetable')
    # SQL диалект может немного меняться
    cur.execute('''
        CREATE TABLE timetable (
            subject_name VARCHAR(255),
            day_of_the_week VARCHAR(255),
            time_of_start time
        )
    ''')


#
# @app.route('/get_next_lesson', methods=['GET'])
# def get_next_lesson():
#     current_day = flask.request.args['current_day']
#     current_time = flask.request.args['current_time']
#     params = dict(dbname="test", user="postgres", password="1234", host="localhost")
#     with psycopg2.connect(**params) as conn:
#         cur = conn.cursor()
#         cur.execute('''SELECT timetable.subject_name, timetable.day_of_the_week, MIN(timetable.time_of_start)
#                         FROM timetable
#                         WHERE timetable.day_of_the_week = %s AND timetable.time_of_start > %s
#                         GROUP BY timetable.subject_name, timetable.day_of_the_week''', (current_day, current_time))
#     for row in cur:
#         return str(row[0])



# @app.route('/get_next_lesson', methods=['GET'])
# def get_next_lesson():
#     current_day = flask.request.args['current_day']
#     current_time = flask.request.args['current_time']
#     params = dict(dbname="test", user="postgres", password="1234", host="localhost")
#     with psycopg2.connect(**params) as conn:
#         cur = conn.cursor()
#         cur.execute('''SELECT timetable.subject_name, timetable.day_of_the_week, MIN(timetable.time_of_start)
#                 FROM timetable
#                 WHERE timetable.day_of_the_week = %s AND timetable.time_of_start > %s
#                 GROUP BY timetable.subject_name, timetable.day_of_the_week''', (current_day, current_time))
#     for row in cur:
#         subject_name, day_of_the_week, time_of_start = row
#         return(subject_name, day_of_the_week, time_of_start)
#



# cur.execute('''
#             INSERT INTO timetable (subject_name, day_of_the_week, time_of_start) VALUES
#                 (%s, %s, %s),
#                     WHERE NOT EXISTS ( SELECT * FROM timetable
#                         WHERE subject_name = %s
#                             AND day_of_the_week = %s
#                                 AND time_of_start = %s)''',
#                                 (subject_name_, day_of_the_week_, time_of_start_, subject_name_, day_of_the_week_, time_of_start_))