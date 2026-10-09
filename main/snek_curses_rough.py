#all ideas here will be transferred into other files and organized cleaner

import time
import curses
from curses import wrapper


def main(main_screen):
    ms = main_screen

#top

#addstr(y,x) I have no idea why???

#size = 22
    
    ms.addstr(2,3,"######################")

#sides
    for n in range(3,15):
        ms.addstr(n,3,"#                    #")
#bot
    ms.addstr(15,3,"######################")
    
    ms.refresh()
 



    i = 5
    y = 4
    
    go_forward = True
    filler = "0"

    ms.timeout(1000)


    while True:

        i += 1

        ms.addstr(y,i, filler)
        
        c = ms.getch()


        if c ==ord('w'):
            break
        if c==ord('s'):
            y = y+1
            i -= 1
        if c==ord('a'):
            break
        if c==ord('d'):
            break
        ms.refresh()
        







#because we're manipulating the term, in order to read our mfin errors we run a try except loop using built in funcs to return the term to normal before displaying our error message. Thus wrapper is born. It's thebuilt in built in that basically handles all the niche shit of trying to return that term back to normal. 

#otherwise we'd have to write our own try excepts n what not. 

wrapper(main)






