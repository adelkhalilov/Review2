# Review2
В начале надо запустить файл data_base.py. Он удаляет базe данных timetable, если она сущетсвовала ранее, и создает новую таблицу с расписанием всех пар : Название предмета, день недели и время начала.
Далее запускается файл server.py и через командную строку подаются запросы вида:
1) ./client.py add_lesson --subject_name {Name of the lesson's subject} --day_of_the_week {name of week's day when lesson will be} --time_of_start {time when lesson will start in hh:mm:ss format}
Собственно это команда для добавления пары в расписание
2) ./client.py get_next_lesson --current_day {Day of the week now} --current_time {Time now in hh:mm:ss format} 
Это команда выдающая какая пара сегодня следующая или что пар сегодня больше нет
3) ./client.py get_lessons 
Команда, которая выводит все расписание на неделю


P.S. Программа написана под Windows
