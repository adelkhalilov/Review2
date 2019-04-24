import argparse
import requests

adres = '127.0.0.1'
PORT = '5000'


def get_args():
    action = None
    subject_name = None
    day_of_the_week = None
    time_of_start = None
    parser = argparse.ArgumentParser()
    subs = parser.add_subparsers(dest='action')
    add = subs.add_parser('add', help='Add')
    add.add_argument('--subject_name', help='subject_name')
    add.add_argument('--day_of_the_week', dest='day_of_the_week', help='Day_of_the_week')
    add.add_argument('--time_of_start', dest='time_of_start', help='Time_of_start')
    get = subs.add_parser('get', help='Get')
    args = parser.parse_args()
    if args.action == 'add':
        action = args.action
        subject_name = args.subject_name
        day_of_the_week = args.day_of_the_week
        time_of_start = args.time_of_start
    if args.action == 'get':
        action = args.action
    return action, subject_name, day_of_the_week, time_of_start

def add_lesson(subject_name, day_of_the_week, time_of_start):
    r = requests.post('http://' + adres + ':' + PORT + '/add_lesson', params={'subject_name': subject_name, 'day_of_the_week': day_of_the_week, 'time_of_start': time_of_start})
    return (r.text)


def get_lessons():
    r = requests.post('http://' + adres + ':' + PORT + '/get_lessons')
    return (r.text)

def main():
    action = ''; subject_name = ''; day_of_the_week = ''; time_of_start = ''
    args = get_args()
    action = args[0]; subject_name = args[1]; day_of_the_week = args[2]; time_of_start = args[3];
    if action == 'add':
        print(add_lesson(subject_name, day_of_the_week, time_of_start))
    if action == 'get':
        print(get_lessons())

if __name__ == '__main__':
    main()