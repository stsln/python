#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    def fill():
        a = 0
        while a != 3:
            move_right()
            fill_cell()
            a += 1

    move_down(2)
    fill()
    move_left()
    move_down()
    fill_cell()
    move_up(2)
    fill_cell()
    move_left()
    pass


if __name__ == '__main__':
    run_tasks()
