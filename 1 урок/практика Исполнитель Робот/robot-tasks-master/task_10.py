#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_3():
    def fill_cel():
        if wall_is_above() or wall_is_beneath():
            fill_cell()
    while not wall_is_on_the_right():
            fill_cel()
            move_right()
    fill_cel()
    pass


if __name__ == '__main__':
    run_tasks()
