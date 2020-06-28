import sys

try:
    sys.exit(1) # Intentionally come out of program
    number = int(input('Enter a number: '))
    print('100 divide by a number {} is {}'.format(number, 100/number))
    print(number + 'String')
except ZeroDivisionError:
    print('Please do not provide 0 as an input')
    try:
        number = int(input('Enter a number: '))
        print('100 divide by a number {} is {}'.format(number, 100 / number))
    except ZeroDivisionError:
        print('Please do not provide 0 as an input.. exiting..')
except TypeError as Err:
    print('Here I am handling the type error: ', Err)
except Exception as E:
    print('Error: ', sys.exc_info()[0], sys.exc_info()[1])
finally:
    print('This block will execute when try block executed successfully..')
