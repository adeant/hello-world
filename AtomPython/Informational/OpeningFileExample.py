with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)

filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
