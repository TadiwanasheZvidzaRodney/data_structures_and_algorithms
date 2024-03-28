name = 'dlroW ecaneM'
reversed_string = ''

last_index = len(name) - 1

while last_index >= 0:
    reversed_string += last_index
    name = name - 1

print(reversed_string)
