#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_6():
    def fill_cel():
        if wall_is_beneath() and not wall_is_above():
            fill_cell()

    while not wall_is_on_the_right():
        fill_cel()
        move_right()
    fill_cel()
    pass


if __name__ == '__main__':
    run_tasks()
