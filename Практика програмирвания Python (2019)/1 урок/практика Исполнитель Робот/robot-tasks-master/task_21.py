#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_down()
    a = 1
    for i in range(13):
        
        while not cell_is_filled():
            move_right(a)
            if not wall_is_on_the_right():
                fill_cell()
            a += 1
        
        move_left()
        while not wall_is_on_the_left():
            fill_cell()
            move_left()
        move_down()
    move_right()
    pass


if __name__ == '__main__':
    run_tasks()
