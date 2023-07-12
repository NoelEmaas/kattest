import sys
from fileProcess import *
from testCases import get_test_cases
from colorama import Fore

def main ():
    parameters = sys.argv[1:]

    if len(parameters) != 2:
        print('Invalid input parameters!')
        exit()

    file_name = parameters[0]
    problem = parameters[1]
    test_cases = get_test_cases(f'https://open.kattis.com/problems/{problem}')

    compile(file_name)

    for index, test_case in enumerate(test_cases):
        print(f'Running sample test case #{index + 1} ...', end='', flush=True)

        output = execute(file_name, test_case['input']).strip()

        if output == test_case['output']:
            print(Fore.GREEN + f'\r✔ Sample test case #{index + 1} passed!', flush=True)
        else:
            print(Fore.RED + f'\r✖ Sample test case #{index + 1} failed!', flush=True)
    

if __name__ == "__main__":
    main()
