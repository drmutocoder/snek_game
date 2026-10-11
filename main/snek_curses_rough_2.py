import curses
import curses.panel
from curses import wrapper
import time
import random


def draw_frame(ms):

    wall_material = "#"
    wall_side_material = "#                #"
    wall_width = 18
    wall_x = 3
    wall_y = 2

    #curses uses y,x for locations
    #top
    ms.addstr(wall_y, wall_x, wall_material * wall_width)

    #middle
    for i in range(wall_x, wall_width):
        ms.addstr(i,wall_x, wall_side_material)
    
    #bottom
    ms.addstr(wall_width, wall_x, wall_material * wall_width)

def draw_win():
    begin_x = 4; begin_y = 3
    height = 15; width = 16
    win = curses.newwin(height, width, begin_y, begin_x)
    return win

def draw_panel(win):
    begin_x = 4; begin_y = 3
    height = 15; width = 16
    panel = curses.panel.new_panel(win)
    return panel


def update_body(snek_arr, target_got_eaten, head_posx, head_posy):
    if len(snek_arr) == 1: 
        snek_arr.insert(0,"0")
        return

    if target_got_eaten == False:
        snek_arr.insert(0,"0")
        return

    if target_got_eaten == True:
        tail = pop(snek_arr(0))
        snek_arr.insert(tail,len(snek_arr))
        return

def head_movement_logic(win,key,head, head_posx, head_posy):

    if key == ord('w'):
        head = "U"
        head_posy -= 1
    
    if key == ord('s'):
        head = "n"
        head_posy += 1

    if key ==  ord('a'):
        head = ")"
        head_posx -= 1

    if key == ord('d'):
        head = "("
        head_posx += 1

    return win.addstr(head_posy, head_posx,head), head_posx, head_posy


def main(main_screen):
    ms = main_screen
    win = draw_win()
    target_win = draw_panel(win)
    win.timeout(1000)

    target = "$"
    target_got_eaten = False
    target_y = 10
    target_x = 10
    target_win.panel.addstr(target_y, target_x, target)


    head_posx = 5
    head_posy = 4

    key = ord('d')
    head = "("

    draw_frame(ms)
    ms.refresh()
    win.refresh()
    

    while True:
        
        if target_got_eaten == True:

            target_y = randint(3,15)
            target_x = randint(4,16)
            target_win.add_str(target_y, target_x, target)
            target_got_eaten = False

        win.clear()
        key = ms.getch()
        head, head_posx, head_posy = head_movement_logic(win,key,head, head_posx, head_posy)
        win.refresh()





wrapper(main)

    
