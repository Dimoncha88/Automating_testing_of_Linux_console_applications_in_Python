from sshcheckers import ssh_checkout, upload_files
import yaml

with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)


def deploy():
    res = []
    upload_files(data.get('host'), data.get('user'), data.get('pswd'), f'{data.get("Folder_in")}{data.get("file")}.deb',
                 f'{data.get("folder_user2")}{data.get("file")}.deb')
    res.append(ssh_checkout(data.get('host'), data.get('user'), data.get('pswd'),
                            f'echo {data.get("pswd")} | sudo -S dpkg -i {data.get("folder_user2")}'
                            f'{data.get("file")}.deb',"Настраивается пакет"))
    res.append(ssh_checkout(data.get('host'), data.get('user'), data.get('pswd'),
                            f'echo {data.get("pswd")} | sudo -S dpkg -s {data.get("file")}',
    "Status: install ok installed"))
    print(res)
    return all(res)


if deploy():
    print("Деплой успешен")
else:
    print("Ошибка деплоя")