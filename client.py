import argparse
import requests
from config import day, PORT, address
from datetime import datetime

now = datetime.now()
weday = now.weekday()
time = now.strftime("%H:%M")


def get_args():
    parser = argparse.ArgumentParser()
    subs = parser.add_subparsers(dest='action', required=True)
    add = subs.add_parser('add_lesson', help='Add_lesson')
    add.add_argument('--subject-name', dest='subject_name', help='subject_name')
    add.add_argument('--day-of-the-week', dest='day_of_the_week', help='Day_of_the_week from {Monday, Tuesday, ... , Sunday}')
    add.add_argument('--time-of-start', dest='time_of_start', help='Time_of_start in format hh:mm')
    get_lessons = subs.add_parser('get_lessons', help='Get_lessons')
    get_next_lesson = subs.add_parser('get_next_lesson', help='Get_next_lesson')
    args = parser.parse_args()
    return args


def add_lesson(subject_name, day_of_the_week, time_of_start):
    r = requests.post('http://' + address + ':' + PORT + '/add_lesson', params={'subject_name': subject_name, 'day_of_the_week': day_of_the_week, 'time_of_start': time_of_start})
    return r.text


def get_lessons():
    r = requests.get('http://' + address + ':' + PORT + '/get_lessons')
    return r.text


def get_next_lesson(current_day, current_time):
    r = requests.get('http://' + address + ':' + PORT + '/get_next_lesson', params={'current_day': current_day, 'current_time': current_time})
    return r.text


def main():
    args = get_args()
    action = args.action
    if action == 'add_lesson':
        print(add_lesson(args.subject_name, args.day_of_the_week, args.time_of_start))
    if action == 'get_lessons':
        print(get_lessons())
    if action == 'get_next_lesson':
        print(get_next_lesson(day[weday], time))

if __name__ == '__main__':
    main()
