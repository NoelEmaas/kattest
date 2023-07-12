import os
import sys
import time
import subprocess


def compile(file_name): 
    curr_dir = os.getcwd()
    name, extension = file_name.split('.')
    compile_command = ''

    if extension == 'cpp':
        compile_command = f'g++ {curr_dir}/{file_name} -o {curr_dir}/{name}'
    elif extension == 'java':
        compile_command = f'javac {file_name}'
    elif extension == 'py':
        return
    else:
        sys.exit('Error: Invalid File Type!')

    try:
        subprocess.run(compile_command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        sys.exit('Compilation Error')



def execute(file_name, input_str):
    time.sleep(1)

    curr_dir = os.getcwd()
    name, extension = file_name.split('.')
    run_command = []

    
    if extension == 'cpp':
        run_command = [f'{curr_dir}/{name}']
    elif extension == 'java':
        run_command = ['java', '-cp', curr_dir, name]
    elif extension == 'py':
        run_command = ['python3', f'{curr_dir}/{file_name}']
    else:
        sys.exit('Error: Invalid File Type!')

    process = subprocess.Popen(
        run_command,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding='utf8')

    stdout, stderr = process.communicate(input=input_str)
    
    if stderr:
        sys.exit(f'Error: {stderr}')
        
    return stdout
