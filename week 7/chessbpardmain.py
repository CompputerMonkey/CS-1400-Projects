'''
    This is the starter file. Only fill in the areas indicated.
    Do not modify existing code.
    Replace this file header with the normal file header (name, etc)
'''

#### Add Import Statement(s) as needed ####
from lib import drawChessboard
#### End Add Import Statement(s) ####

def main():
    #### Add Code to get input from user ####
    startpos = input("Enter start position (x, y) ")
    startX, startY = map(int, startpos.split(', '))
    startX, startY = ((startX, startY))
    width = input("width ")
    height = input("height ")
    #### End Add Code to get input from user ####

    if width == "" and height == "":
        drawChessboard(startX, startY)
    elif height == "":
        drawChessboard(startX, startY, width=eval(width))
    elif width == "":
        drawChessboard(startX, startY, height=eval(height))
    else:
        drawChessboard(startX, startY, eval(width), eval(height))


main()