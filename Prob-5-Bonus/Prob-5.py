# Module 7
#   Programming Assignment 10
#     Prob-5.py

# <Garrett>

from graphics import * 


def main():
    win = GraphWin("Event Loop", 500, 500)

    circle = Circle(win.getMouse(), 50)
    circle.setFill("red")
    circle.setOutline("red")
    circle.draw(win)

    pt = win.getMouse()
    circ = circle.getCenter()

    count = 1
    endFlag = False

    while True:
        coords = win.checkMouse()
        if coords != None:
            handleClick(win, circ, count, pt)
            count += 1
        if endFlag is False:
            break
    return circle

def handleClick(win, circ, count, pt):
    if count <= 5:
        dx = pt.getX() - circ.getX()
        dy = pt.getY() - circ.getY()
        circle.move(dx, dy)
        endFlag = False
        print(dx)
        print(dy)
        return endFlag
    else: 
        endFlag = True
        return endFlag



main()