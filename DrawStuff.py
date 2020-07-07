#############################################################
# File Name : DrawStuff.py
#
#             Draw_Stuff Class
#             draws a Line given two points
#
# Created :   April 2020 
#############################################################

from kivy.graphics import InstructionGroup
from kivy.graphics import Color
from kivy.graphics import Line

##############################################################
##############################################################

class Draw_Stuff():

    #################################################
    def __init__(self, **kwargs):
        self.IG_Line = InstructionGroup()

    #################################################
    # Clear all the Instructions from the IG_Line
    # and make the Labels invisible
    def Clear_Lines(self):
        self.IG_Line.clear()

    #################################################
    # Draw a Line inside the Drawing Window Area
    # given Pixel coordinates
    # Not Axis Coordinates
    def Draw_Line(self, pScreen=None, pX1=0, pY1=0, pX2=0, pY2=0, pR=1, pG=1, pB=1, pW=1, pOp=1):
        self.IG_Line.add(Color(rgba = (pR, pG, pB, pOp)))
        self.IG_Line.add(Line(points = [pX1, pY1, pX2, pY2], width = pW))
        if(pScreen is not None):
            pScreen.canvas.before
            pScreen.canvas.add(self.IG_Line)
        return

    #################################################
    def Draw_Rectangles(self, pScreen=None, pXo=0, pXf=100, pYo=0, pYf=100, pR=1, pG=1, pB=0, pOffset=0):
        for x in range(pXo, pXf, 6):
            x3 = x + pOffset
            self.Draw_Line(pScreen, x3, pYo, x3, pYf, pR, pG, pB, 2)
            pScreen.canvas.ask_update()
        return

##############################################################
##############################################################


