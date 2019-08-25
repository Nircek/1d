#!/usr/bin/env python3
import curses
from _curses import error
from time import time
scr = curses.initscr()
curses.noecho()
curses.cbreak()
scr.keypad(True)
scr.nodelay(True)
curses.curs_set(False)
s = curses.COLS-2
p1 = 'O'
p2 = 'X'
p1s = '+'
p2s = '-'
l = ' '*s
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
    scr.addstr('\N{FULL BLOCK}')
    scr.addstr(''.join(map(lambda x: ' ' if x==' ' else '\N{FULL BLOCK}', l)))
    scr.addstr('\N{FULL BLOCK}')
    scr.refresh()
    while t+0.1>time():
        pass
    half = (curses.COLS-2)//2
    if l[0] == p2s:
        scr.erase()
        scr.addstr(half*' '+half*'\N{FULL BLOCK}')
        return False
    if l[-1] == p1s:
        scr.erase()
        scr.addstr(half*'\N{FULL BLOCK}')
        return False
    return True

try:
    while main():
        pass
    scr.nodelay(False)
    scr.getkey()
finally:
    curses.nocbreak()
    scr.keypad(False)
    curses.echo()
    curses.endwin()
