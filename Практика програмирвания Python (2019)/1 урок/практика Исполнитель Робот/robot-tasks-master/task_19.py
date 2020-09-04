#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    a = 0
    while not wall_is_on_the_left() and wall_is_above():
        move_left()
    if wall_is_above():
        a += 1
        while not wall_is_on_the_right() and wall_is_above():
            move_right()
        if wall_is_above():
            a += 1
        else:
            while not wall_is_above():
                move_up()
            while not wall_is_on_the_left():
                move_left()
    else:
        while not wall_is_above():
            move_up()
    if a == 2:
        pass
        
    pass


if __name__ == '__main__':
    run_tasks()
