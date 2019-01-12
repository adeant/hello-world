done = 0
prompt = 'Write a positive number'

while done != 1:
    number = input(prompt)
    number = int(number)
    if number > 0:
        print('nice')
        done = 1
    else:
        print('try again')
