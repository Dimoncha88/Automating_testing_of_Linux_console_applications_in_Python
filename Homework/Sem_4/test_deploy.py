import pytest
from sshcheckers import ssh_checkout, upload_files
import yaml

with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)


def test_deploy():
    res = []
    upload_files(data.get('host'), data.get('user'), data.get('pswd'), f'{data.get("Folder_in")}{data.get("file")}.deb',
                 f'{data.get("folder_user2")}{data.get("file")}.deb')
    res.append(ssh_checkout(data.get('host'), data.get('user'), data.get('pswd'),
                            f'echo {data.get("pswd")} | sudo -S dpkg -i {data.get("folder_user2")}'
                            f'{data.get("file")}.deb',"Настраивается пакет"))
    res.append(ssh_checkout(data.get('host'), data.get('user'), data.get('pswd'),
                            f'echo {data.get("pswd")} | sudo -S dpkg -s {data.get("file")}',
    "Status: install ok installed"))
    assert all(res)


def test_make_archive(make_folders, make_files):
    assert ssh_checkout(data.get('host'), data.get('user'), data.get('pswd'),
                        f'echo {data.get("pswd")}; cd {data.get("folder_in_user2")}; '
                        f'7z a {data.get("folder_out_user2")}/arch_1', 'Everything is Ok')


def test_extract_files():
    assert ssh_checkout(data.get('host'), data.get('user'), data.get('pswd'),
                        f'echo {data.get("pswd")}; cd {data.get("folder_out_user2")}; 7z x arch_1.7z',
                        'Everything is Ok')


def test_delete(delete_folders):
    assert ssh_checkout(data.get('host'), data.get('user'), data.get('pswd'),
                            f'echo {data.get("pswd")} | sudo -S dpkg -r {data.get("file")}',
    "Удаляется")


if __name__ == '__main__':
    pytest.main(['-vv'])
