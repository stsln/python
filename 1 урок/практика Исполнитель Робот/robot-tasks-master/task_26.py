#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    i = 1
    while i != 6:
        i += 1

        n = 0
        while n < 10:
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
            if n == 10:
                move_left()
            else:
                move_right(3)

        if i == 6:
            move_left(36)
        else:
            move_left(36)
            move_down(4)
        
    pass


if __name__ == '__main__':
    run_tasks()
