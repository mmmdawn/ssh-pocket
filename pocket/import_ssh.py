import sys
import json
from os import path

HOME_DIR = path.expanduser('~')


def main():
    args = sys.argv
    if len(args) != 2:
        return

    with open(args[1], 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        lines = [line for line in lines if line]

    ssh_dict = {}
    for line in lines:
        components = line.split('@')
        name = components[0]
        user = components[1]
        ip = components[2]

        if name not in ssh_dict:
            ssh_dict[name] = {
                'ip': ip,
                'users': [user]
            }
        elif ssh_dict[name]['ip'] != ip:
            return
        else:
            ssh_dict[name]['users'].append(user)

    ssh_dict = {k: v for k, v in sorted(ssh_dict.items(), key=lambda item: item[0])}
    with open(f'{HOME_DIR}/.ssh/pocket.json', 'w') as f:
        json.dump(ssh_dict, f)


if __name__ == '__main__':
    main()
