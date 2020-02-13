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

"""
move_left()	Пройти n клеток влево (по умолчанию n = 1)
move_right()	Пройти n клеток вправо (по умолчанию n = 1)
move_up()	Пройти n клеток вверх (по умолчанию n = 1)
move_down()	Пройти n клеток вниз (по умолчанию n = 1)
wall_is_above()	если сверху стена, возвращает True, иначе — False
wall_is_beneath()	если снизу стена, возвращает True, иначе — False
wall_is_on_the_left()	если слева стена, возвращает True, иначе — False
wall_is_on_the_right()	если справа стена, возвращает True, иначе — False
fill_cell()	Закрасить текущую клетку
cell_is_filled()	Возвращает True, если текущая клетка закрашена
mov(r, v)	Поместить значение v в регистр r
"""
