import curses
from curses import wrapper
import random
import time





def main(main_screen):

    begin_x = 10
    begin_y = 3
    height = 15
    width = 20

    win = curses.newwin(height, width, begin_y, begin_x)

    win.box()
    win.refresh()
    win.timeout(1000)
    head = "("
    headx = 5
    heady = 5


    while True:

        key = win.getch()
        if key == ord('w'):
            head = "U"
            heady -= 1
        if key == ord('s'):
            head = "n"
            heady += 1
        if key == ord('a'):
            head = ")"
            headx -= 1
        if key == ord('d'):
            head = "("
            headx += 1


        win.addstr(heady,headx,head)

    
wrapper(main)
