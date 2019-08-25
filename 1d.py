import curses
from _curses import error
from time import time
scr = curses.initscr()
curses.noecho()
curses.cbreak()
scr.keypad(True)
scr.nodelay(True)
s = curses.COLS-2
p1 = 'O'
p2 = 'X'
p1s = '+'
p2s = '-'
l = ' '*s
p = ''
def main():
    global p,l
    t = time()
    l = l.replace('+-', '  ').replace('+ ', ' +').replace(' -', '- ')
    try:
        p = ''
        p = str(scr.getkey())
    except:
        pass
    if p == 'KEY_LEFT':
        l = p1s + l[1:]
    if p == 'KEY_RIGHT':
        l = l[:-1] + p2s
    scr.erase()
    scr.addstr(p1)
    scr.addstr(l)
    scr.addstr(p2)
    scr.addstr(p)
    scr.refresh()
    while t+0.2>time():
        pass
    return True

try:
    while main():
        pass
finally:
    curses.nocbreak()
    scr.keypad(False)
    curses.echo()
    curses.endwin()
