#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    move_right()
    b = 0
    def a():
        if not wall_is_above():
            a = 0
            while not wall_is_above():
                move_up(n=1)
                fill_cell()
                a += 1
            move_down(a)
    while not wall_is_on_the_right():
        if not wall_is_above():
            a()
            move_right()
        else:
           move_right()
        b += 1
    else:
        a()
    move_left(b + 1)
    pass


if __name__ == '__main__':
    run_tasks()
