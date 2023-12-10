'''
Условие:
Дополнить проект фикстурой, которая после каждого шага теста дописывает в
заранее созданный файл stat.txt строку вида: время, кол-во файлов из конфига,
размер файла из конфига, статистика загрузки процессора из файла /proc/loadavg
(можно писать просто всё содержимое этого файла).
'''

import pytest
from Seminar.Sem_2.task1 import func_return_bool
import yaml

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


@pytest.mark.usefixtures('make_folders', 'make_files', 'append_text_to_file')
class TestSeminar:

    def test_make_archive(self):
        assert func_return_bool(f'cd {data.get("Folder_in")}; 7z a {data.get("Folder_out")}/arch_1', 'Everything is Ok')

    def test_list_archive(self):
        assert func_return_bool(f'cd {data.get("Folder_out")}; 7z l arch_1.7z', 'Listing archive:')

    def test_extract_files(self):
        assert func_return_bool(f'cd {data.get("Folder_out")}; 7z x arch_1.7z', 'Everything is Ok')

    def test_delete_archive(self):
        assert func_return_bool(f'cd {data.get("Folder_out")}; 7z d arch_1', 'Everything is Ok')


if __name__ == '__main__':
    pytest.main(['-vv'])
