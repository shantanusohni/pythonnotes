
count = 1
while count <= 5:

    try:
        number = int(input('Enter a number: '))
        print('100 divide by a number {} is {}'.format(number, 100/number))
        break
    except ZeroDivisionError:
        print('Please do not provide 0 as an input')
    count += 1