#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    same_floor = 0
    while same_floor < 2:
        while not wall_is_beneath():
            move_down()
            same_floor = 0
        while not wall_is_on_the_right():
            move_right()
        while not wall_is_on_the_left():
            if not wall_is_beneath():
                move_down()
                same_floor = 0
            move_left()
        same_floor += 1
    pass


if __name__ == '__main__':
    run_tasks()
