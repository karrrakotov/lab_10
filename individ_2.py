#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json

#   Использовать словарь, содержащий следующие ключи: название пункта назначения; номер
#   поезда; время отправления. Написать программу, выполняющую следующие действия: ввод
#   с клавиатуры данных в список, состоящий из словарей заданной структуры; записи должны
#   быть упорядочены по времени отправления поезда; вывод на экран информации о поездах,
#   направляющихся в пункт, название которого введено с клавиатуры; если таких поездов нет,
#   выдать на дисплей соответствующее сообщение.


def n_add():
    location = input("Название пункта назначения: ")
    train = int(input("Номер поезда: "))
    time = input("Время отправления: ")

    train = {
        'location': location,
        'train': train,
        'time': time,
    }

    trains.append(train)
    if len(trains) > 1:
        trains.sort(key=lambda item: item.get('train', ''))


def n_list():
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 17
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^17} |'.format(
            "№",
            "Пункт назначения",
            "Номер поезда",
            "Время отправления"
        )
    )
    print(line)

    for idx, train in enumerate(trains, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>17} |'.format(
                idx,
                train.get('location', ''),
                train.get('train', ''),
                train.get('time', 0)
            )
        )

    print(line)


def n_select():
    parts = command.split(' ', maxsplit=2)

    number = str(parts[1])

    count = 0
    for train in trains:
        if train.get('location') == number:
            count += 1
            print('Пункт назначения:', train.get('location', ''))
            print('Номер поезда:', train.get('train', ''))
            print('Время отправления:', train.get('time', ''))

    if count == 0:
        print("Таких мест нет!")


def n_load():
    # Разбить команду на части для выделения имени файла.
    parts = command.split(' ', maxsplit=1)

    # Прочитать данные из файла JSON.
    with open(parts[1], 'r') as f:
        global trains
        trains = json.load(f)


def n_save():
    # Разбить команду на части для выделения имени файла.
    parts = command.split(' ', maxsplit=1)

    # Сохранить данные в файл JSON.
    with open(parts[1], 'w') as f:
        json.dump(trains, f)


def n_help():
    print("Список команд:\n")
    print("add - добавить поезд;")
    print("list - вывести список поездов;")
    print("select <номер поезда> - запросить информацию о выбранном поезде;")
    print("help - отобразить справку;")
    print("load <имя файла> - загрузить данные из файла;")
    print("save <имя файла> - сохранить данные в файл;")
    print("exit - завершить работу с программой.")


def n_error():
    print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    trains = []

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

        elif command.startswith('load '):
            n_load()

        elif command.startswith('save '):
            n_save()

        elif command == 'help':
            n_help()

        else:
            n_error()
