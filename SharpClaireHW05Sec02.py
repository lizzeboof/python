# Project:      Homework #5 (SharpClaireHW05Sec02.py)
# Name:         Claire "Boof" Sharp
# Date:         11/28/16
# Description:  This program lets the user roll up to five dice.
#               It also keeps track of their score and allows them
#               to exit at any time.

from graphics import *
import random

def getClick(UI,intXPos):
    # Makes the two buttons on the interface work!
    run = 1
    while run == 1:
        clickpos = UI.getMouse()
        if clickpos.getX() in range(intXPos,(intXPos+80)) and clickpos.getY() in range(20,100):
            intRN = random.randint(1,6)
            run = 0
        elif clickpos.getX() in range(480,580) and clickpos.getY() in range(220,260):
            UI.close()
            run = 0
        else:
            run = 1
    return intRN

def dieBuild(UI,intRN,intXPos):
    # Sets everything up to be drawn.
    die = Rectangle(Point(intXPos,20),Point((intXPos+80),100))
    pipUL = Circle(Point(intXPos+20,40),5)
    pipUR = Circle(Point(intXPos+60,40),5)
    pipML = Circle(Point(intXPos+20,60),5)
    pipM = Circle(Point(intXPos+40,60),5)
    pipMR = Circle(Point(intXPos+60,60),5)
    pipBL = Circle(Point(intXPos+20,80),5)
    pipBR = Circle(Point(intXPos+60,80),5)

    # Colours things in because you can't do that while defining for some reason.
    die.setFill('#3F1F00')
    pipUR.setFill('#CF8F4F')
    pipUL.setFill('#CF8F4F')
    pipML.setFill('#CF8F4F')
    pipM.setFill('#CF8F4F')
    pipMR.setFill('#CF8F4F')
    pipBL.setFill('#CF8F4F')
    pipBR.setFill('#CF8F4F')

    # Draws the die which corresponds to our random number.
    die.draw(UI)
    if intRN == 1:
        pipM.draw(UI)
    elif intRN == 2:
        pipBL.draw(UI)
        pipUR.draw(UI)
    elif intRN == 3:
        pipBL.draw(UI)
        pipM.draw(UI)
        pipUR.draw(UI)
    elif intRN == 4:
        pipUR.draw(UI)
        pipUL.draw(UI)
        pipBL.draw(UI)
        pipBR.draw(UI)
    elif intRN == 5:
        pipUL.draw(UI)
        pipUR.draw(UI)
        pipM.draw(UI)
        pipBL.draw(UI)
        pipBR.draw(UI)
    else:
        pipUL.draw(UI)
        pipUR.draw(UI)
        pipML.draw(UI)
        pipMR.draw(UI)
        pipBL.draw(UI)
        pipBR.draw(UI)

def main():
    # Opens a UI window. Chocolate flavoured.
    UI = GraphWin('Dice Game',600,280)
    UI.setBackground('#BF6F3F')

    # In case the "X" in the corner breaks.
    exitBtn = Rectangle(Point(480,220),Point(580,260))
    exitBtn.setFill('#8F3F1F')
    exitBtn.draw(UI)
    Text(Point(530,240),"Quit").draw(UI)

    # Rolls five dice! How fun!
    runcount = 0
    intRollTotal = 0
    for run in range(5):
        intXPos = 20+(100*runcount)

        # Draws the button to roll the next die.
        rollBtn = Rectangle(Point(intXPos,20),Point((intXPos+80),100))
        rollBtn.setFill('#8F3F1F')
        rollBtn.draw(UI)
        rollLbl = Text(Point((intXPos+40),60),"Roll!")
        rollLbl.draw(UI)

        # Generates a random number, then uses it to build a corresponding die.
        intRN = getClick(UI,intXPos)
        dieBuild(UI,intRN,intXPos)

        # Adds text stating the current total rolled.
        intRollTotal += intRN
        if runcount > 0:
            rollTotal.undraw()
        rollTotal = Text(Point(150,200),("Your Score is: "+str(intRollTotal)))
        rollTotal.setSize(24)
        rollTotal.setStyle('bold')
        rollTotal.draw(UI)

        # Deletes the previous roll button,
        rollBtn.undraw()
        rollLbl.undraw()

        # Ticks up the run counter
        runcount += 1

    # Waits for mouse input, then closes the window after 5 dice have been rolled.
    UI.getMouse()
    UI.close()

main()
