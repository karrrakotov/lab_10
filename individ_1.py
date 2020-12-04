#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

#   Использовать словарь, содержащий следующие ключи: фамилия и инициалы; номер группы;
#   успеваемость (список из пяти элементов).
#   Написать программу, выполняющую следующие действия:
#   ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
#   записи должны быть упорядочены по алфавиту;
#   вывод на дисплей фамилий и номеров групп для всех студентов, имеющих хотя бы одну оценку 2;
#   если таких студентов нет, вывести соответствующее сообщение.


def n_add():
    n = 5
    name = input("Введите фамилию и имя: ")
    group = input("Введите группу: ")
    global marks
    marks = list(
        map(int, input("Введите пять оценок, которые получил студент, в формате - x y z: ").split(None, n)[:n]))

    for mark in marks:
        if mark < 2 or mark > 5:
            print("Такой оценки не существует, введите значение от 1 до 5!", file=sys.stderr)
            exit(1)

    person = {
        'name': name,
        'group': group,
        'marks': marks,
    }

    students.append(person)
    if len(students) > 1:
        students.sort(key=lambda item: item.get('name', ''))


def n_list():
    line = '+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 8,
        '-' * 8,
        '-' * 8,
        '-' * 8,
        '-' * 8,
        '-' * 11
    )
    print(line)
    print(
        '| {:^3} | {:^30} | {:^20} | {:^8} | {:^8} | {:^8} | {:^8} | {:^8} |'.format(
            "№",
            "Ф.И.О.",
            "Группа",
            "1-ая оценка",
            "2-ая оценка",
            "3-ая оценка",
            "4-ая оценка",
            "5-ая оценка"
        )
    )
    print(line)
    # Вывести данные о всех сотрудниках.
    for idx, person in enumerate(students, 1):
        print(
            '| {:>3} | {:<30} | {:<20} | {:>11} | {:>11} | {:>11} | {:>11} | {:>11} |'.format(
                idx,
                person.get('name', ''),
                person.get('group', ''),
                person.get('marks[0]', f'{marks[0]}'),
                person.get('marks[1]', f'{marks[1]}'),
                person.get('marks[2]', f'{marks[2]}'),
                person.get('marks[3]', f'{marks[3]}'),
                person.get('marks[4]', f'{marks[4]}')
            )
        )
    print(line)


def n_select():
    parts = command.split(' ', maxsplit=2)

    count = 0
    for person in students:
        if 2 in marks:
            count += 1
            print(
                '{:>4}: {}'.format(count, person.get('name', ''))
            )
    # Если счетчик равен 0, то работники не найдены.
    if count == 0:
        print("Нет студентов, которые получили оценку - 2.")


def n_help():
    # Вывести справку о работе с программой.
    print("Список команд:\n")
    print("add - добавить студента;")
    print("list - вывести список студентов;")
    print("select <оценка> - найти студентов которые получили такую оценку;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


def n_error():
    print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':

    marks = 0
    students = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            n_add()

        elif command == 'list':
            n_list()

        elif command.startswith('select '):
            n_select()

        elif command == 'help':
            n_help()

        else:
            n_error()

