# Расписание занятий
В начале надо запустить файл data_base.py. Он удаляет базу данных timetable, если она сущетсвовала ранее, и создает новую таблицу с расписанием всех пар : Название предмета, день недели и время начала.
Далее запускается файл server.py и через командную строку подаются запросы вида:
1) ./client.py add_lesson --subject-name {Name of the lesson's subject} --day-of-the-week {name of week's day when lesson will be} --time-of-start {time when lesson will start in hh:mm format}
. Это собственно команда для добавления пары в расписание

2) ./client.py get_next_lesson
. Это команда выдающая какая пара сегодня следующая или что пар сегодня больше нет

3) ./client.py get_lessons 
. Команда, которая выводит все расписание на неделю


P.S. Программа написана под Windows
