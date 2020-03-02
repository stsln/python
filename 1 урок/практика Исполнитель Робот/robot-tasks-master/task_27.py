#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    move_right()
    fill_cell()
    
    a = 0
    b = a

    while wall_is_on_the_right() == False:
        if a < b:
            a += 1
            move_right()
        else:
            a = 0
            b += 1
            move_right()
            if not wall_is_on_the_right():
                fill_cell()
    pass


if __name__ == '__main__':
    run_tasks()
