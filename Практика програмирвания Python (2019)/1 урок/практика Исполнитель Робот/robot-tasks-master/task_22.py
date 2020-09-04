#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    a = True
    while a == True:
        while not wall_is_on_the_right():
            fill_cell()
            move_right()
        fill_cell()

        if wall_is_on_the_right() and wall_is_beneath():
            a = False
            while not wall_is_on_the_left():
                move_left()
        else:
            a = True
            while not wall_is_on_the_left():
                move_left()
            move_down()
    pass


if __name__ == '__main__':
    run_tasks()
