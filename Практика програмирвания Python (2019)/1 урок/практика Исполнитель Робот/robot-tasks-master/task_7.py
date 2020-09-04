#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_4():
    score = 0
    while not wall_is_beneath():
        move_down()
    while wall_is_beneath():
        score += 1
        move_right()
    move_down()
    move_left(score)
    pass


if __name__ == '__main__':
    run_tasks()
