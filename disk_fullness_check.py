import shutil
import subprocess
import argparse
import time

red = '\033[31m'
green = '\033[32m \033[4m'
yellow = '\033[33m'

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--threshold_value', default=False, help='Threshold value of free on disk in percent')
    parser.add_argument('-c', '--exec_command', default=False, help='The command is executed after reaching the threshold')
    parser.add_argument('-t', '--check_time', default=False, help='Check time in seconds')
    script_arg = parser.parse_args()
    return script_arg

def check_disk():
    data = shutil.disk_usage("/")
    return data

def check_free_space(data):
    free_space = (data.free / data.total) * 100
    return free_space

def call_command(command):
    subprocess.call(f'{command}', shell=True)

def value_compare(free_space):
    print(f'{yellow}Free space: {free_space}\nThreshold value: {THRSHOLD_VALUE}')
    if free_space < THRSHOLD_VALUE: return False
    else: return True

def main():
    while True:
        data = check_disk()
        free_space = check_free_space(data)

        if value_compare(free_space):
            time.sleep(CHECK_TIME)
        else: 
            call_command(EXEC_COMMAND)
            time.sleep(CHECK_TIME)

if __name__ == '__main__':
    script_arg = create_parser()

    THRSHOLD_VALUE = int(script_arg.threshold_value)
    EXEC_COMMAND = script_arg.exec_command
    CHECK_TIME = int(script_arg.check_time)

    main()
    