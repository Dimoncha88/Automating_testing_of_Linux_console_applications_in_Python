'''
Задание 1.

Условие:
Написать функцию на Python, которой передаются в качестве параметров команда и текст.
Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и
False в противном случае. Передаваться должна только одна строка, разбиение вывода использовать
не нужно.
'''

import subprocess


def func_return_bool(text: str):
    result = subprocess.run(text, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if result.returncode == 0:
        return '22.04' in out and 'jammy' in out


print(func_return_bool('cat /etc/os-release'))
