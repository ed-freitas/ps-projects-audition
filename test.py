import os
import sys
import difflib

def diff(file1, file2):
    with open(file1) as f1:
        f1_text = f1.read()
    with open(file2) as f2:
        f2_text = f2.read()

    line = ''
    for line in difflib.unified_diff(f1_text, f2_text, fromfile=file1, tofile=file2, lineterm=''):
        break
    
    if line != '':
        print('Error: ' + file1 + ' does not contain the expected input. Please check ' + file2)

def run(args):
    try: 
        if len(args) == 2:
            if args[1] in ['t1_2.py', 't3.py', 't4.py', 't5.py', 't6.py', 't7.py', 't8.py', 't9.py']:
                diff(args[1], args[1].replace('.py', '.txt'))
    except BaseException as msg:
        print('An error occured... :( ' + str(msg))

if __name__ == '__main__':
    run(sys.argv)