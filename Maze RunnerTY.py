#!/usr/bin/env python3
""" Copyright © 2020 Tyler Shackelford
Program derived from tdemo_fractalCurves.py in
the turtle-example-suite.

The CurvesTurtle class and the fractal-curve-
methods are taken from the PythonCard example
scripts for turtle-graphics.
"""
from turtle import *
from time import sleep, perf_counter as clock
import random
coords = []
xpath = []
arraydirections = ["1234"]
BOARDWIDTH = None
BOARDHEIGHT = None
SIZE = None
maxheight = 396
maxwidth = 471
#maxheight = 300
#maxwidth = 400
visible = False
while BOARDWIDTH is None:
    pxl = "Enter the board width (20 to {xx}): ".format(xx = maxwidth)
    print(pxl)
    BOARDWIDTH = input()
    try:
        if int(BOARDWIDTH)>= 20 and int(BOARDWIDTH) <=maxwidth:
            BOARDWIDTH = int(BOARDWIDTH)
            break
        else:
            BOARDWIDTH = None 
    except:
        BOARDWIDTH = None

while BOARDHEIGHT is None:
    pxl = "Enter the board height (20 to {xx}): ".format(xx = maxheight)
    print(pxl)
    BOARDHEIGHT = input()
    try:
        if int(BOARDHEIGHT)>= 20 and int(BOARDHEIGHT) <=maxheight:
            BOARDHEIGHT = int(BOARDHEIGHT)
            break
        else:
            BOARDHEIGHT = None
    except:
        BOARDHEIGHT = None

screensize(BOARDWIDTH, BOARDHEIGHT)





maxsize = int(min(BOARDWIDTH, BOARDHEIGHT)/2)
while SIZE is None:
    pxl = "Enter the maze gap (2 to {xx}): ".format(xx = maxsize)
    print(pxl)
    SIZE = input()
    try:
        if int(SIZE)>= 1 and int(SIZE) <=maxsize:
            SIZE = int(SIZE)
            break
        else:
            SIZE = None
    except:
        SIZE = None

def changedirection(xloc, yloc):
    if pen()["pendown"]:
        end_fill()
        up()
    else:
        down()
        begin_fill()
        
def retinv(direction):
    if direction == "1":
        return "3"
    elif direction == "2":
        return "4"
    elif direction == "3":
        return "1"
    else:
        return "2"

def changecolor():
    a = random.randint(0, 255)

def randomdirection(directions):
    x = random.randint(0, len(directions)-1)
    return directions[x]
    
def hilbert(xloc, yloc, level):
    changecolor()
    newcoords = [xloc,yloc]
    setpos(newcoords)
    coords = []
    coords.append([xloc,yloc])
    xpath = ["0"]
    skipper = False
    breaker = False
    arraydirections = ["1234","1234"]
    """#Makes border
    up()
    setpos(-BOARDWIDTH, -BOARDHEIGHT)
    down()
    setpos(-BOARDWIDTH, BOARDHEIGHT)
    setpos(BOARDWIDTH, BOARDHEIGHT)
    setpos(BOARDWIDTH, -BOARDHEIGHT)
    setpos(-BOARDWIDTH, -BOARDHEIGHT)
    up()"""
    setpos(0,0)
    down()
    while level > 0:
        skipper = False
        while len(arraydirections[level]) > 0:
            direction = randomdirection(arraydirections[level])
            newcoords = newcoord(direction, newcoords)
            invdirection = retinv(direction)
            arraydirections[level] = arraydirections[level].replace(direction, "")
            if not newcoords in coords:
                coords.append(newcoords)
                [xloc,yloc] = newcoords
                makeline(direction)
                xpath.append(direction)
                arraydirections.append(arraydirections[0])
                level = level + 1
                arraydirections[level] = arraydirections[0]
                arraydirections[level] = poploc(arraydirections[level],newcoords)
                testcoords = newcoords
                for i in range(3):
                    testdirection = str(i + 1)
                    testcoord = newcoord(testdirection, testcoords)
                    if testcoord in coords:
                        arraydirections[level].replace(testdirection, "")
                skipper = True
                break
            else:
                changecolor()
                newcoords = [xloc,yloc]
                skiptest = True
                breaker = True
                
        if len(xpath) <= 1:
            return
        if skipper == False:
            changecolor()
            direction = xpath.pop()
            direction = retinv(direction)
            newcoords = newcoord(direction, newcoords)
            [xloc,yloc] = newcoords
            makeline(direction)            
            level = level - 1
            arraydirections[level] = arraydirections[0]
            arraydirections[level] = poploc(arraydirections[level],newcoords)
            testcoords = newcoords
            for i in range(3):
                testdirection = str(i + 1)
                testcoord = newcoord(testdirection, testcoords)
                if testcoord in coords:
                    arraydirections[level].replace(testdirection, "")
            if level < 1:
                breakpoint()
        else:
            skipper = False
            
def newcoord(direction, newcoords):
    newx = newcoords[0]
    newy = newcoords[1]
    if direction == "1":
        newy = int(newcoords[1]) + SIZE
    elif direction == "2":
        newx = int(newcoords[0]) + SIZE
    elif direction == "3":
        newy = int(newcoords[1]) - SIZE
    else:
        newx = int(newcoords[0]) - SIZE
    return [newx,newy]
        
def poploc(directions, newcoords):
    xrep = directions
    if newcoords[0] <= -BOARDWIDTH:
        xrep = xrep.replace("4","")
    elif newcoords[0] >= BOARDWIDTH:
        xrep = xrep.replace("2","")
    if newcoords[1] <= -BOARDHEIGHT:
        xrep = xrep.replace("3","")
    elif newcoords[1] >= BOARDHEIGHT:
        xrep = xrep.replace("1","")        
    return xrep
    
def makeline(direction):
    if direction == "1":
        sety(ycor() + SIZE)
    elif direction == "2":
        setx(xcor() + SIZE)
    elif direction == "3":
        sety(ycor() - SIZE)
    elif direction == "4":
        setx(xcor() - SIZE)
    else:
        breakpoint()
    
def randomdirection(directions):
        x = random.randint(0, len(directions)-1)
        return directions[x]
    
def main():
    i = 0
    #screensize(BOARDWIDTH, BOARDHEIGHT)
    while i < 1:
        i = i + 1
        speed(0)
        ht()
        wn = Screen()
        rootwindow = wn.getcanvas().winfo_toplevel()
        rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
        rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
        #visible = True
        getscreen().tracer(1,0)
        pu()
        setpos(0, 0)
        pd()
        ta=clock()
        fillcolor("red")
        home()
        xd = 0
        level = 1
        hilbert(0, 0, level)
    return 

if __name__  == '__main__':
    msg = main()
    mainloop()
