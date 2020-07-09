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
        self.IG_Line  = InstructionGroup()

    #################################################
    # Clear all the Instructions in IG_Line
    def Clear_IG(self):
        self.IG_Line.clear()

    #################################################
    # Draw a Line inside the Drawing Window Area
    # given Pixel coordinates
    # Not Axis Coordinates
    def Draw_Line(self, pIG=None, pX1=0, pY1=0, pX2=0, pY2=0, pR=1, pG=1, pB=1, pW=1, pOp=1):
        pIG.add(Color(rgba = (pR, pG, pB, pOp)))
        pIG.add(Line(points = [pX1, pY1, pX2, pY2], width = pW))
        return

    #################################################
    def Draw_Frame(self, pScreen=None, pXo=0, pXf=100, pYo=0, pYf=100):
        self.Draw_Line(pIG=self.IG_Line, pX1=pXo, pY1=pYo, pX2=pXo, pY2=pYf, pR=0, pG=0.39, pB=0.49, pW=3)
        self.Draw_Line(pIG=self.IG_Line, pX1=pXo, pY1=pYf, pX2=pXf, pY2=pYf, pR=0, pG=0.39, pB=0.49, pW=3)
        self.Draw_Line(pIG=self.IG_Line, pX1=pXf, pY1=pYo, pX2=pXf, pY2=pYf, pR=0, pG=0.39, pB=0.49, pW=3)
        self.Draw_Line(pIG=self.IG_Line, pX1=pXo, pY1=pYo, pX2=pXf, pY2=pYo, pR=0, pG=0.39, pB=0.49, pW=3)
        return

    #################################################
    def Draw_ManyLines(self, pScreen=None, pXo=0, pXf=100, pYo=0, pYf=100, pR=1, pG=1, pB=0, pOffset=0):
        for x in range(pXo, pXf, 6):
            x3 = x + pOffset
            self.Draw_Line(pIG=self.IG_Line, pX1=x3, pY1=pYo, pX2=x3, pY2=pYf, pR=pR, pG=pG, pB=pB, pW=2)
        return
    
    #################################################
    def Show_Instructions(self, pScreen=None):
        if(pScreen is not None):
#            pScreen.canvas.clear()
            pScreen.canvas.add(self.IG_Line)
            pScreen.canvas.ask_update()
        return

##############################################################
##############################################################


