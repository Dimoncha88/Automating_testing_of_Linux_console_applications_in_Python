'''
Задание 1.

Условие:
Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и
разархивирования с путями (x).
'''

import pytest
from Seminar.Sem_2.task1 import func_return_bool


folder_in = '/home/dk/Folder_in'
folder_out = '/home/dk/Folder_out'
folder_ex = '/home/dk/Folder_ex'


def test_make_archive():
    assert func_return_bool(f'cd {folder_in}; 7z a {folder_out}/arch_1', 'Everything is Ok')


# def test_delete_archive():
#     assert func_return_bool(f'cd {folder_out}; 7z d arch_1', 'Everything is Ok')


def test_list_archive():
    assert func_return_bool(f'cd {folder_out}; 7z l arch_1.7z', 'Listing archive:')


def test_extract_files():
    assert func_return_bool(f'cd {folder_out}; 7z x arch_1.7z', 'Everything is Ok')


if __name__ == '__main__':
    pytest.main(['-vv'])
