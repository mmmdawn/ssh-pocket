# SSH Pocket

## Installation
```
pip install ssh-pocket
```

## Prerequisite

File `$HOME/.ssh/pocket.json` with following form:
```
{
  "Test server": {
    "ip": "123.124.12.1",
    "users": ["root", "test"]
  },
  "Test server 1": {
    "ip": "12.12.12.12",
    "users": ["root", "test1", "test2", "infinity"]
  }
}
```

## Usage

Use command `s` in terminal.