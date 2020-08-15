# Name: Bradley Kangas
# Date: 4/28/2020
# Assignment 3: Yahtzee
# This program plays Yahtzee using buttons and dice
#
import turtle
import random

# Set global variables
dMainList = []
bMainList = []
win = turtle.Screen()
mTurt = turtle.Turtle()

#main function
#Sets up window, listener, dice, buttons, then draws the dice and buttons
#Parameters: None
#Variables:
#   dMainList   | global list used to store dice
#   bMainList   | global list used to store buttons
#   dSubList1-5 | sublists that contain values the dice will use
#   bSubList1-5 | sublists that contain values the buttons will use
#
def main():
    global dMainList
    global bMainList
    global mTurt
    win.bgcolor("cornflowerblue")
    turtle.setup(1200, 600)
    mTurt.hideturtle()
    mTurt.speed(0)
    win.onclick(mouseClick, 1, True)

    #Set up dice
    dSubList1 = [0, 0, 0, 0, ""]
    dSubList2 = [0, 0, 0, 0, ""]
    dSubList3 = [0, 0, 0, 0, ""]
    dSubList4 = [0, 0, 0, 0, ""]
    dSubList5 = [0, 0, 0, 0, ""]
    dMainList = [dSubList1, dSubList2, dSubList3, dSubList4, dSubList5]

    #Set up buttons
    bSubList1 = [-200, -150, 100, 50, "black", "grey", "Roll"]
    bSubList2 = [-50, -150, 100, 50, "black", "grey", "New-Roll"]
    bMainList = [bSubList1, bSubList2]

    #Draw dice and set values
    for dSubList in dMainList:
        dSubList[0] = random.randrange(1, 6, 1)
        dSubList[1] = (-425 + dMainList.index(dSubList) * 1.5 * 100)
        dSubList[2] = 0
        dSubList[3] = 100
        dSubList[4] = "white"
        drawDie(mTurt, dSubList[0], dSubList[1], dSubList[2], dSubList[3], dSubList[4])

    #Draw the buttons
    for bSubList in bMainList:
        drawRectangle(mTurt, bSubList[0], bSubList[1], bSubList[2], bSubList[3], bSubList[4], bSubList[5], bSubList[6])

    turtle.mainloop()

#mouseClick function
#Gets where the user clicked and runs isWithin() for each button/dice
#Parameters:
#   mX          | x coordinate of mouse position
#   mY          | y coordinate of mouse position
#Variables:
#   dMainList   | global list used to store dice
#   bMainList   | global list used to store buttons
# 
def mouseClick(mX, mY):
    global dMainList
    global bMainList

    #Iterate list of buttons
    for bSubList in bMainList:
        if (isWithin(mX, mY, bSubList[0], bSubList[1], bSubList[2], bSubList[3]) == True):
            buttonClick(bMainList.index(bSubList))

    #Iterate list of dice
    for dSubList in dMainList:
        if (isWithin(mX, mY, dSubList[1], dSubList[2], dSubList[3], dSubList[3]) == True):
            dieClick(dMainList.index(dSubList))

#isWithin function
#Compares given coordinates with coordinates of buttons/dice
#Determines if given coordinates are within the buttons/dice
#Parameters:
#   x   | x value to check
#   y   | y value to check
#   a   | the x value of button/dice
#   b   | the y value of the button/dice
#   w   | the width of the button/dice
#   h   | the height of the button/dice
#Variables: None
#
def isWithin(x, y, a, b, w, h):
    if ((x > a) and (x < a + w) and (y < b) and (y > b - h)):
        return True
    else:
        return False

#buttonClick function
#Determines which button is clicked
#Button 1 ignores all colors other than white and rolls dice
#Button 2 rolls all dice
#Parameters:
#   index       | index of button in bMainList
#Variables:
#   dMainList   | global list used to store dice
#   bMainList   | global list used to store buttons
#   mTurt       | global turtle used to drawDie
#
def buttonClick(index):
    global dMainList
    global bMainList
    global mTurt
    if (index == 0):
        for dSubList in dMainList:
            if dSubList[4] == "white":
                dSubList[0] = random.randrange(1, 6, 1)
                drawDie(mTurt, dSubList[0], dSubList[1], dSubList[2], dSubList[3], dSubList[4])
    else:
        for dSubList in dMainList:
            dSubList[4] = "white"
            dSubList[0] = random.randrange(1, 6, 1)
            drawDie(mTurt, dSubList[0], dSubList[1], dSubList[2], dSubList[3], dSubList[4])

#dieClick function
#Determines which die was clicked and sets color based on existing color
#Parameters:
#   index       | index of button in bMainList
#Variables:
#   dMainList   | global list used to store dice
#   mTurt       | global turtle used to drawDie
#   dieClicked  | the die clicked in dMainList
#
def dieClick(index):
    global dMainList
    global mTurt
    dieClicked = dMainList[index]
    if dieClicked[4] == "white":
            dieClicked[4] = "red"
    else:
            dieClicked[4] = "white"
    drawDie(mTurt, dieClicked[0], dieClicked[1], dieClicked[2], dieClicked[3], dieClicked[4])

#drawRectangle function
#Draws a rectangle based on multiple given parameters
#Parameters:
#   turt    | the turtle used to draw the shape
#   x       | x coordinate to draw at
#   y       | y coordinate to draw at
#   width   | width of rectangle
#   height  | height of rectangle
#   lColor  | line color of rectangle
#   fColor  | fill color of rectnagle
#   text    | text to put inside rectangle (defaults to None)
#Variables: None
#
def drawRectangle(turt, x, y, width, height, lColor, fColor, text = None):
    turt.penup()
    turt.setpos(x,y)
    turt.pencolor(lColor)
    turt.fillcolor(fColor)
    turt.pendown()
    turt.begin_fill()
    
    # Draw rectangle shape
    for i in range(2):
        turt.forward(width)
        turt.right(90)
        turt.forward(height)
        turt.right(90)

    turt.end_fill()
    turt.penup()

    # Writes text if text exists
    if (text != None):
        turt.setpos(x + width/2, y - height/2)
        turt.write(text, align="center", font=("Helvetica", 12, "bold"))

#drawDie function
#Draws the dice and then calls the drawDots() function to draw dots on the dice
#Parameters:
#   d     | the turtle used to draw the dice and dots
#   value | the number of dots that appear
#   x     | the location on the window to draw the dice (x coordinate)
#   y     | the location of the window to draw the dice (y coordinate)
#   width | the size of the dice
#   color | the color of the dice
#Variables: None
#
def drawDie(d, value, x, y, width, color):
    d.penup()
    d.setpos(x, y)

    #Draw the box
    d.pencolor("black")
    d.fillcolor(color)
    d.pendown()
    d.begin_fill()
    for i in range(4):
        d.forward(width)
        d.right(90)
    d.end_fill()
    d.penup()

    drawDots(d, value, x, y, width)

#drawDot function
#Calculates how to draw dots on each die, then calls turtleDot() to actually draw them
#Parameters:
#   d         | the turtle used to draw the dice and dots
#   value     | the number of dots that appear
#   x         | the location on the window to draw the dice (x coordinate)
#   y         | the location of the window to draw the dice (y coordinate)
#   diceWidth | the size of the dice
#Variables:
#   spacing  | used for positioning the dots within the dice at intervals of 1/4 (0.25)
#   dotSize  | used for scaling the size of the dots correctly with the size of the die
#
def drawDots(d, value, x, y, diceWidth):
    #Set turtle values for the dice
    d.pencolor("black")
    d.fillcolor("black")
    spacing = 0.25
    dotSize = diceWidth // 6
    
    #Check if odd or one, since all odd sides of dice has dot in the middle
    if value % 2 == 1 or value == 1:
        d.setpos((x + diceWidth * (spacing * 2)), (y - diceWidth * (spacing * 2)))
        turtleDot(d, dotSize)

    if value > 1:
        #Draw dot at bottom left / top right
        d.setpos((x + diceWidth * (spacing * 3)), (y - diceWidth * (spacing)))
        turtleDot(d, dotSize)
        d.setpos((x + diceWidth * (spacing)), (y - diceWidth * (spacing * 3)))
        turtleDot(d, dotSize)

        if value > 2:
            if value == 3:
                return
            #Draw dot at the top left / bottom right
            d.setpos((x + diceWidth * (spacing)), (y - diceWidth * (spacing)))
            turtleDot(d, dotSize)
            d.setpos((x + diceWidth * (spacing * 3)), (y - diceWidth * (spacing * 3)))
            turtleDot(d, dotSize)

            if value > 4:
                if value == 5:
                    return
                #Draw dot in the middle left / middle right
                d.setpos((x + diceWidth * (spacing)), (y - diceWidth * (spacing * 2)))
                turtleDot(d, dotSize)
                d.setpos((x + diceWidth * (spacing * 3)), (y - diceWidth * (spacing * 2)))
                turtleDot(d, dotSize)

#turtleDot function
#Does turtle operations for drawing the dots on the dice
#Exists as a shortcut so I don't have to type this out repeatedly
#Parameters:
#   turtle   | the turtle used to draw the dice and dots
#   size     | the size of the dots to draw
#Variables: None
#
def turtleDot(turtle, size):
    turtle.pendown()
    turtle.begin_fill()
    turtle.dot(size)
    turtle.end_fill()
    turtle.penup()
    
if __name__ == "__main__":
    main()
