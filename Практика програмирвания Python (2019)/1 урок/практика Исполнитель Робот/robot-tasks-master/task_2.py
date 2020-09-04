#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_2():
    for i in range(3):
        if i == 2:
            fill_cell()
            move_right()
            move_down()
        else:
            move_right()
            move_down()
    pass
    move_right()


if __name__ == '__main__':
    run_tasks()
