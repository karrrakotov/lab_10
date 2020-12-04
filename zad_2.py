#!/usr/bin/env python3
# -*- config: utf-8 -*-

import math


#   Решите следующую задачу: в основной ветке программы вызывается функция cylinder(),
#   которая вычисляет площадь цилиндра. В теле cylinder() определена функция circle(),
#   вычисляющая площадь круга по формуле . В теле cylinder() у пользователя
#   спрашивается, хочет ли он получить только площадь боковой поверхности цилиндра,
#   которая вычисляется по формуле , или полную площадь цилиндра. В последнем
#   случае к площади боковой поверхности цилиндра должен добавляться удвоенный результат
#   вычислений функции circle().

def cylinder():
    def circle():
        result = math.pi * r ** 2
        return result

    s_cylinder = 2 * math.pi * r * h
    s_circle = s_cylinder + 2 * (math.pi * r ** 2)

    a = input('Получить боковую площадь - 1, или полную - 2? - ')
    if a == '1':
        print(s_cylinder)
    elif a == '2':
        circle()
        full = s_circle
        print(full)


if __name__ == '__main__':
    s_circle = 0
    r = float(input("Введите радиус: "))
    h = float(input("Введите высоту: "))

    cylinder()
