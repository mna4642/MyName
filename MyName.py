"""CSCI-603: Lab 1
    Author: Michael Abdelshahid

    This is a demo of my name in MIIKEY
"""

import turtle as mike

# global constants for window dimensions
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

def init():
    """
    Initialize for drawing.  (-200,-800) is in the lower left and
    (800, 800) is in the upper right.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """
    mike.setworldcoordinates(-WINDOW_WIDTH/2, -WINDOW_WIDTH*2, WINDOW_WIDTH*2, WINDOW_HEIGHT*2)

def M():
    """
    Make the letter M.
    :pre:(relative) pos(0,0)
    :post:(relative) pos(0,0)
    :return: None
    """
    mike.hideturtle()
    mike.Screen()
    mike.speed(0)
    mike.left(90)
    mike.forward(180)
    mike.right(157.5)
    mike.forward(180)
    mike.left(135)
    mike.forward(180)
    mike.right(157.5)
    mike.forward(180)
    mike.left(90)
    mike.up()
    mike.forward(50)
    mike.down()

def I():
    """
    Make the two letters I.
    :pre:(relative) pos(0,0)
    :post:(relative) pos(0,0)
    :return: None
    """
    mike.penup()
    mike.pendown()
    mike.Screen()
    mike.speed(0)
    mike.left(90)
    mike.forward(180)
    mike.left(90)
    mike.up()
    mike.back(50)
    mike.left(90)
    mike.forward(180)
    mike.left(90)

def K():
    """
    Make the letter K.
    :pre:(relative) pos(0,0)
    :post:(relative) pos(0,0)
    :return: None
    """
    mike.Screen()
    mike.speed(50)
    mike.penup()
    mike.pendown()
    mike.left(90)
    mike.forward(180)
    mike.left(180)
    mike.forward(90)
    mike.left(135)
    mike.forward(112.5)
    mike.left(180)
    mike.forward(112.5)
    mike.left(90)
    mike.forward(135)
    mike.left(45)
    mike.up()
    mike.forward(50)
    mike.down()

def E():
    """
    Make the letter E.
    :pre:(relative) pos(0,0)
    :post:(relative) pos(0,0)
    :return: None
    """
    mike.Screen()
    mike.speed(0)
    mike.penup()
    mike.pendown()
    mike.left(90)
    mike.forward(180)
    mike.right(90)
    mike.forward(90)
    mike.right(180)
    mike.forward(90)
    mike.left(90)
    mike.forward(90)
    mike.left(90)
    mike.forward(90)
    mike.left(180)
    mike.forward(90)
    mike.left(90)
    mike.forward(90)
    mike.left(90)
    mike.forward(90)
    mike.up()
    mike.forward(50)
    mike.down()

def main():
    """
    The main function.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """
    init()
    M()
    I()
    K()
    E()
    mike.mainloop()

main()
