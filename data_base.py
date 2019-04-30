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
