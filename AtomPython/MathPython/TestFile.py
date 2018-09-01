'''
Find the factors of an integer
'''
def factors(b):
    for i in range(1, b+1):
        if b % i == 0:
            print('{0} x {1} = {2}'.format(i, (b/i), b))

if __name__ == '__main__':
    b = input('Your Number Please: ')
    try:
        b = float(b)
    except ValueError:
        pass

    if b > 0 and b.is_integer():
        factors(int(b))
    else:
        print('Please enter a positive integer')
