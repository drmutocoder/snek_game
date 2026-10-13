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
    win.timeout(150)
    head = "("
    headx = 5
    heady = 5

    target = "%"
    targetx = random.randint(0,14)
    targety = random.randint(0,19)

    prev_key = ord('d')

    snek = [(headx, heady),(headx-1, heady),(headx-2, heady)]
    length = 3 


    while True:

        if snek[0] in snek[1:]:
            break
    
        if snek[0] == (targetx, targety):
            while True:
                targetx = random.randint(1, width - 2)
                targety = random.randint(1, height - 2)
                if (targetx, targety) not in snek:
                    length += 1
                    break

        key = win.getch()
        if key != -1:
            prev_key = key
        if key == -1:
            key = prev_key

        body_y = heady
        body_x = headx

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

        snek.insert(0, (headx,heady))
        if len(snek) > length:
            space = snek.pop(len(snek)-1)
            (x,y) = space
            win.addstr(y,x," ")


        win.addstr(targety,targetx,target)
        win.addstr(body_y,body_x,"0")
        win.addstr(heady,headx,head)

    
wrapper(main)
