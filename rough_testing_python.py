import sys


def testcase1():
    print('Hello from utilts')
    print(f'loaded{__file__}')

if __name__== '__main__':
    print(f" Yes python file has been loaded")
    # print('python:', sys.executable)
    testcase1()