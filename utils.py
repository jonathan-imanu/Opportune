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
        
