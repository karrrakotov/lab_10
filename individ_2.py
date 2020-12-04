#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
import json
import sys


def add(staff, location, train, time):
    # Создать словарь.
    train = {
        'location': location,
        'train': train,
        'time': time,
    }

    # Добавить словарь в список.
    staff.append(train)
    # Отсортировать список в случае необходимости.
    if len(staff) > 1:
        staff.sort(key=lambda item: item.get('location', ''))


def list(staff):
    table = []
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 8
    )
    table.append(line)
    table.append(
        '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
            "№",
            "Пункт назначения",
            "Номер поезда",
            "Время отправления"
        )
    )
    table.append(line)

    # Вывести данные о всех сотрудниках.
    for idx, train in enumerate(trains, 1):
        table.append(
            '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                idx,
                train.get('location', ''),
                train.get('train', ''),
                train.get('time', 0)
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
    for train in trains:
        if train.get('location') == number:
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
    trains = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о работнике.
            location = input("Название пункта назначения: ")
            train = int(input("Номер поезда: "))
            time = input("Время отправления: ")

            add(trains, location, train, time)

        elif command == 'list':
            print(list(trains))

        elif command.startswith('select '):
            # Разбить команду на части для выделения номера года.
            parts = command.split(maxsplit=1)
            # Получить список работников.
            selected = select(train, str(parts[1]))

            # Вывод списка работников.
            if selected:
                for idx, location in enumerate(selected, 1):
                    print('{:>4}: {}'.format(idx, location.get('location', '')))
            else:
                print("Таких мест нет!")

        elif command.startswith('load '):
            # Разбить команду на части для имени файла.
            parts = command.split(maxsplit=1)
            # Загрузить данные из файла
            trains = load(parts[1])

        elif command.startswith('save '):
            # Разбить команду на части для имени файла.
            parts = command.split(maxsplit=1)
            # Сохранить данные в файл
            save(trains, parts[1])

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить пункт назначения;")
            print("list - вывести список работников;")
            print("select <стаж> - запросить работников со стажем;")
            print("load <имя_файла> - загрузить данные из файла;")
            print("save <имя_файла> - сохранить данные в файл;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
