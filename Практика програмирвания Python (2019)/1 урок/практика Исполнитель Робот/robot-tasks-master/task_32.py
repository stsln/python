#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    count_filled_cells = 0
    while wall_is_beneath():

        #красим клетки которые между вверхней и нижней стенок
        if wall_is_above() and wall_is_beneath():
            fill_cell()    
        move_right()

        #добавление в ax
        if not wall_is_beneath() and not wall_is_above():
            mov("ax", count_filled_cells)
            return
        
        #проверка верхней стены
        if not wall_is_above():
            #поднимаемеся вверх
            while not wall_is_above():
                move_up(n=1)
                if cell_is_filled():
                    count_filled_cells += 1
                fill_cell()
            #опускаемся вниз
            while not wall_is_beneath():
                move_down(n=1)
    pass


if __name__ == '__main__':
    run_tasks()
