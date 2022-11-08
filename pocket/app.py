import json
import subprocess
from os import system, name, path

from InquirerPy import inquirer
from InquirerPy.base.control import Choice


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def connect(ip, user):
    command = 'ssh'
    conn = f'{user}@{ip}'
    subprocess.run([command, conn])


class App:
    def __init__(self):
        home = path.expanduser('~')
        with open(f'{home}/.ssh/pocket.json', 'r') as f:
            self.ssh_dict = json.load(f)

        if not self.ssh_dict:
            self.ssh_dict = {}

    def home(self) -> None:
        while True:
            clear()
            choice = inquirer.fuzzy(
                message="Select:",
                choices=[
                    Choice(value=None, name="Exit"),
                    *self.ssh_dict
                ]
            ).execute()
            clear()

            if choice:
                server = choice
                ip = self.ssh_dict[server]["ip"]
                action = inquirer.select(
                    message='Choose user:',
                    choices=[
                        *self.ssh_dict[server]["users"],
                        'Back'
                    ]
                ).execute()

                if action == 'Back':
                    continue
                else:
                    connect(ip, action)

            else:
                print('\nEasy peasy\n')
                break

    def run(self):
        self.home()
