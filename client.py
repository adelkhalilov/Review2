import argparse
import requests

address = '127.0.0.1'
PORT = '5000'


def get_args():
    parser = argparse.ArgumentParser()
    subs = parser.add_subparsers(dest='action')
    add = subs.add_parser('add_lesson', help='Add_lesson')
    add.add_argument('--subject_name', help='subject_name')
    add.add_argument('--day_of_the_week', dest='day_of_the_week', help='Day_of_the_week')
    add.add_argument('--time_of_start', dest='time_of_start', help='Time_of_start')
    get_lessons = subs.add_parser('get_lessons', help='Get_lessons')
    get_next_lesson = subs.add_parser('get_next_lesson', help='Get_next_lesson')
    get_next_lesson.add_argument('--current_day', dest='current_day', help='Current_day')
    get_next_lesson.add_argument('--current_time', dest='current_time', help='Current_time')
    args = parser.parse_args()
    if args.action == 'add_lesson':
        return args.action, args.subject_name, args.day_of_the_week, args.time_of_start, None, None
    if args.action == 'get_lessons':
        return args.action, None, None, None, None, None
    if args.action == 'get_next_lesson':
        return args.action, None, None, None, args.current_day, args.current_time


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
    action = ''; subject_name = ''; day_of_the_week = ''; time_of_start = ''
    current_day = ''; current_time = ''
    args = get_args()
    action = args[0]; subject_name = args[1]; day_of_the_week = args[2]; time_of_start = args[3];
    current_day = args[4]; current_time = args[5]
    if action == 'add_lesson':
        print(add_lesson(subject_name, day_of_the_week, time_of_start))
    if action == 'get_lessons':
        print(get_lessons())
    if action == 'get_next_lesson':
        print(get_next_lesson(current_day, current_time))

if __name__ == '__main__':
    main()
