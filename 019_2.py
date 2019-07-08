try:
    num = int(input("Enter: "))
    print(10 / num)

except ZeroDivisionError:
    print('Enter number except ')

except ValueError:
    print('Input number ')
