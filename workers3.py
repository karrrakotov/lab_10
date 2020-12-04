#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import sys


def add(staff, name, person, marks):
    # Создать словарь.
    person = {
        'name': name,
        'person': person,
        'marks': marks,
    }


    # Добавить словарь в список.
    staff.append(person)
    # Отсортировать список в случае необходимости.
    if len(staff) > 1:
        staff.sort(key=lambda item: item.get('name', ''))


def list(staff):
    table = []
    # Заголовок таблицы.
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
    table.append(line)
    table.append(
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
    table.append(line)

    # Вывести данные о всех сотрудниках.
    for idx, person in enumerate(students, 1):
        table.append(
            '| {:>3} | {:<30} | {:<20} | {:>11} | {:>11} | {:>11} | {:>11} | {:>11} |'.format(
                idx,
                person.get('name', ''),
                person.get('person', ''),
                person.get('marks[0]', f'{marks[0]}'),
                person.get('marks[1]', f'{marks[1]}'),
                person.get('marks[2]', f'{marks[2]}'),
                person.get('marks[3]', f'{marks[3]}'),
                person.get('marks[4]', f'{marks[4]}')
            )
        )

    table.append(line)

    return '\n'.join(table)


def select(staff, period):
    # Инициализировать результат.
    result = []
    number = str(parts[1])
    # Проверить сведения работников из списка.
    count = 0
    for person in students:
        if person.get('name') == number:
            count += 1

    return result


def load(filename):
    with open(filename, 'r') as fin:
        return json.load(fin)


def save(staff, filename):
    with open(filename, 'w') as fout:
        json.dump(staff, fout)


if __name__ == '__main__':
    # Список работников.
    students = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о работнике.
            n = 5
            name = input("Введите фамилию и имя: ")
            person = input("Введите группу: ")
            marks = list(map(int, input("Введите пять оценок, которые получил студент, в формате - x y z: ").split(None, n)[:n]))

            add(students, name, person, marks)


        elif command == 'list':
            print(list(students))

        elif command.startswith('select '):
            # Разбить команду на части для выделения номера года.
            parts = command.split(maxsplit=1)
            # Получить список работников.
            selected = select(students, int(parts[1]))

            # Вывод списка работников.
            if selected:
                for idx, person in enumerate(selected, 1):
                    print('{:>4}: {}'.format(idx, person.get('name', '')))
            else:
                print("Нет студентов, которые получили оценку - 2.")

        elif command.startswith('load '):
            # Разбить команду на части для имени файла.
            parts = command.split(maxsplit=1)
            # Загрузить данные из файла
            students = load(parts[1])

        elif command.startswith('save '):
            # Разбить команду на части для имени файла.
            parts = command.split(maxsplit=1)
            # Сохранить данные в файл
            save(students, parts[1])

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить студента;")
            print("list - вывести список студентов;")
            print("select <оценка> - найти студентов которые получили такую оценку;")
            print("load <имя_файла> - загрузить данные из файла;")
            print("save <имя_файла> - сохранить данные в файл;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
