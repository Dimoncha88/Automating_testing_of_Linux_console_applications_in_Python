import pytest
import yaml
from Seminar.Sem_2.task1 import func_return_bool

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


@pytest.fixture(scope='class')
def make_folders():
    return func_return_bool(f'mkdir -p {data.get("Folder_in")} {data.get("Folder_out")} {data.get("Folder_ex")}', '')


@pytest.fixture(scope='class')
def delete_folders():
    yield
    return func_return_bool(f'rm -rf {data.get("Folder_in")} {data.get("Folder_out")} '
                            f'{data.get("Folder_ex")}', '')


@pytest.fixture(scope='class')
def make_files():
    return func_return_bool(f'cd {data.get("Folder_in")}; touch file1.txt file2.txt file3.txt', '')


@pytest.fixture(scope='function')
def append_text_to_file():
    return func_return_bool(f'date >> stat.txt; cat /proc/loadavg >> stat.txt', '')
