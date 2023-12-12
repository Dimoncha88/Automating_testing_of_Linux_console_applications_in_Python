import pytest
import yaml
from sshcheckers import ssh_checkout

with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def make_folders():
    return ssh_checkout(data.get('host'), data.get('user'), data.get('pswd'),
                f'echo {data.get("pswd")} | mkdir -p {data.get("folder_in_user2")} {data.get("folder_out_user2")} '
                            f'{data.get("folder_ex_user2")}', '')


@pytest.fixture()
def delete_folders():
    yield
    return ssh_checkout(data.get('host'), data.get('user'), data.get('pswd'),
                        f'echo {data.get("pswd")} | rm -rf {data.get("folder_in_user2")} {data.get("folder_out_user2")} '
                        f'{data.get("folder_ex_user2")}', '')


@pytest.fixture()
def make_files():
    return ssh_checkout(data.get('host'), data.get('user'), data.get('pswd'),
                        f'echo {data.get("pswd")}; cd {data.get("folder_in_user2")}; '
                        f'touch file1.txt file2.txt file3.txt', '')
