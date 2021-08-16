import shutil
import subprocess
import argparse
import time

red = '\033[31m'
green = '\033[32m \033[4m'
yellow = '\033[33m'

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--free_space_threshold', default=False, help='Threshold value of used on disk in percent')
    parser.add_argument('-c', '--exec_command', default=False, help='The command is executed after reaching the threshold')
    parser.add_argument('-t', '--check_time', default=False, help='Check time in seconds')
    script_arg = parser.parse_args()
    return script_arg

def check_disk():
    data = shutil.disk_usage("/")
    return data

def check_used_space(data):
    used_space = round(98 - (data.free / data.total) * 100)
    return used_space

def call_command(command):
    subprocess.call(f'{command}', shell=True)

def main():
    while True:
        data = check_disk()
        used_space = check_used_space(data)
        print(f'{yellow}Free space: {used_space}%\nThreshold value: {FREE_SPACE_THRSHOLD}%')

        if used_space < FREE_SPACE_THRSHOLD:
            time.sleep(CHECK_TIME)
        else: 
            call_command(EXEC_COMMAND)
            time.sleep(CHECK_TIME)

if __name__ == '__main__':
    script_arg = create_parser()

    FREE_SPACE_THRSHOLD = int(script_arg.free_space_threshold)
    EXEC_COMMAND = script_arg.exec_command
    CHECK_TIME = int(script_arg.check_time)

    main()