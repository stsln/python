#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_1():
    for i in range(1):
        move_right(2)
        move_down()
    pass


if __name__ == '__main__':
    run_tasks()
