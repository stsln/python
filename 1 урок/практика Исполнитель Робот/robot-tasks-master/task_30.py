#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_9_3():
    size_field = 0
    while not wall_is_on_the_right():
        move_right()
        size_field += 1
    
    move_left(size_field)

    while size_field > 1:
        count = 0
        while 1:
            move_right()
            count += 1
            if count == size_field:
                break
            fill_cell()
        count = 0
        while 1:
            move_down()
            count += 1
            if count == size_field:
                break
            fill_cell()
        count = 0
        while 1:
            move_left()
            count += 1
            if count == size_field:
                break
            fill_cell()
        count = 0
        while 1:
            move_up()
            count += 1
            if count == size_field:
                break
            fill_cell()
        size_field -= 2
        move_down()
        move_right()
    while not wall_is_beneath() and not wall_is_on_the_left():
        move_left()
        move_down()
    pass


if __name__ == '__main__':
    run_tasks()

"""
move_left(n=1)	Пройти n клеток влево (по умолчанию n = 1)
move_right(n=1)	Пройти n клеток вправо (по умолчанию n = 1)
move_up(n=1)	Пройти n клеток вверх (по умолчанию n = 1)
move_down(n=1)	Пройти n клеток вниз (по умолчанию n = 1)
wall_is_above()	если сверху стена, возвращает True, иначе — False
wall_is_beneath()	если снизу стена, возвращает True, иначе — False
wall_is_on_the_left()	если слева стена, возвращает True, иначе — False
wall_is_on_the_right()	если справа стена, возвращает True, иначе — False
fill_cell()	Закрасить текущую клетку
cell_is_filled()	Возвращает True, если текущая клетка закрашена
mov(r, v)	Поместить значение v в регистр r
"""
