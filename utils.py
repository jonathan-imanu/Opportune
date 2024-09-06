import subprocess
from datetime import datetime

def update_env_variable(key, new_value):
    with open('.env', 'r') as file:
        lines = file.readlines()

    variable_updated = False
    for i, line in enumerate(lines):
        if line.startswith(key + '='):
            lines[i] = f'{key}={new_value}\n'
            variable_updated = True
            break

    if not variable_updated:
        lines.append(f'{key}={new_value}\n')

    with open('.env', 'w') as file:
        file.writelines(lines)
        
def get_row_number():
    with open('row_number.txt', 'r') as file:
        row_number = int(file.read())
    return row_number

def update_row_number(row_number):
    with open('row_number.txt', 'w') as file:
        file.write(str(row_number))

def get_time_of_last_run():
    line = subprocess.check_output(['tail', '-1', "logs.txt"]).decode("utf-8")
    last_run = datetime.strptime(line.split(" ")[0], "%m/%d/%H:%M,%f")
    last_run = last_run.replace(datetime.now().year)
    return last_run
