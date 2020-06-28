import os
import sys

dir_path = input('Enter a directory path: ')
filename = input('Enter a filename: ')

try:
    abspath = os.path.join(dir_path, filename)
    backup = os.path.join(dir_path, filename+'.bck')
    if not os.path.isfile(abspath):
        raise FileExistsError('File not found') # Raise is Python function
    with open(abspath, 'r') as infile:
        with open(backup, 'w') as outfile:
            outfile.write(infile.read())
except Exception as E:
    print('Error: ', E, sys.exc_info()[0])
finally:
    if 'infile' in globals():
        infile.close()

    if 'outfile' in globals():
        outfile.close()