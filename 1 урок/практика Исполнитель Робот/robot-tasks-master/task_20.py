#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    b = 0
    while b < 6:
        a = 54
        b += 1
        move_right()
        while a > 27:
            fill_cell()
            move_right()
            a -= 1
        move_down()
        move_left()
        while a > 0:
            fill_cell()
            move_left()
            a -= 1
        move_down()
    move_right()
    pass


if __name__ == '__main__':
    run_tasks()
