n = input('Enter the number: ')

try:
    n = int(n)
    print(10/int(n))
except ZeroDivisionError:
    print('Error!')
