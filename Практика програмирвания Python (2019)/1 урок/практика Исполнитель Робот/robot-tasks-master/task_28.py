#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    a = 0
    b = True
    while b == True:
        if a == 5:
            b = False
        else:
            move_right()
        if cell_is_filled():
            a += 1
    pass


if __name__ == '__main__':
    run_tasks()
