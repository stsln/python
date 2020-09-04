#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    a = 0
    b = True
    while b == True:
        if a == 3 or wall_is_on_the_right():
            b = False
        else:
            move_right()
        if cell_is_filled():
            a += 1
        else:
            a = 0
    pass


if __name__ == '__main__':
    run_tasks()
