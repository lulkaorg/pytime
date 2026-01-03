#!/usr/bin/env python3

from datetime import datetime, timedelta
import os
import signal
import sys

def main():
    home_dir = os.path.expanduser('~')
    log_file = os.path.join(home_dir, 'work_time.txt')

    start = datetime.now()
    print(f'{start.strftime("%A, %d.%m.%Y")}\n'
          f'Started working at {start.strftime("%H:%M")}')

    input('Hit Enter if you are done working')

    end = datetime.now()
    #end_8 = end + timedelta(hours=8)
    print(f'Stopped working at {end.strftime("%H:%M")}')

    time_diff = end - start
    breaktime = int(input('Enter break time in minutes: '))
    worktime = time_diff - timedelta(minutes=breaktime)
    print(f'Worked for {worktime} hours')

    log_content = (
        f'{start.strftime("%A, %d.%m.%Y")}\n'
        f'Started working: {start}\n'
        f'Stopped working: {end}\n'
        f'Break time: {breaktime} minutes\n'
        f'Worktime: {worktime}\n'
        f'{"-" * 50}\n'
    )

    with open(log_file, 'a') as f:
        f.write(log_content)

    print(f'Saved to {log_file}')


if __name__ == '__main__':
    main()
