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

Or use `si` command to create the above `json` file:
```
si $FILE
```
 `$FILE` is a file with format:
```
Test server 1@root@123.123.123.123
Test server 2@someone@12.12.12.12
Test server 3@admin@13.13.13.13
```
## Usage

Use command `s` in terminal.
