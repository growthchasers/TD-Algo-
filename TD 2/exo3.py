import re
equation = input("entre l'equation (format: ax + b): ")
ax, b = equation.split('+')
match = re.match(r"(-?\d*)([a-zA-Z]+)", ax)
if match:
    a = match.group(1) or '1'
    x = match.group(2) or 'x'
    a, b = map(int, [a, b.strip()])
    result = float(- b / a)
    print(f'x = {result}')
else:
    print('invalid format.')
