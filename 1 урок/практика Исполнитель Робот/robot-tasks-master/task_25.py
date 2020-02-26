#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    move_down()
    n = 0
    while n < 5:
        n += 1
        def fill():
            a = 0
            while a != 2:
                fill_cell()
                a += 1
                move_right()
                fill_cell()
        move_down()
        fill()
        move_left()
        move_down()
        fill_cell()
        move_up(2)
        fill_cell()
        if n == 5:
            move_left()
        else:
            move_right(3)
    
    pass


if __name__ == '__main__':
    run_tasks()
