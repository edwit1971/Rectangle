#############################################################
# File Name : DrawStuff.py
#
#             Draw_Stuff Class
#             draws a Line given two points and then draws
#             X and Y component Lines and displays their
#             values in an overlapping Label
#
# Created :   April 2020 
#############################################################

import math

from kivy.logger   import Logger
from kivy.graphics import InstructionGroup
from kivy.graphics import Color
from kivy.graphics import Line
from kivy.graphics import Point

##############################################################
##############################################################

class Draw_Stuff():

    #################################################
    def __init__(self, **kwargs):
        ##########################
        String1 = 'Draw_Stuff: def __init__'
        Logger.info(String1)
        ##########################
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
    def Draw_Point(self, pScreen=None, pX=0, pY=0, pR=1, pG=1, pB=1, pW=1, pOp=1):
        self.IG_Line.add(Color(rgba = (pR, pG, pB, pOp)))
        self.IG_Line.add(Point(points = [pX, pY], pointsize = pW))
        if(pScreen is not None):
            pScreen.canvas.before
            pScreen.canvas.add(self.IG_Line)
        return

    #################################################
    def Draw_CFP_Circle(self, pScreen=None, pXo=0, pXf=100, pYo=0, pYf=100, pC=0, pF=0, pP=0):
        Xc = pXo + int((pXf - pXo) * 0.5)
        Yc = pYo + int((pYf - pYo) * 0.5)
        Pi = 3.141592653589793
        Two_Pi = Pi * 2.0
        Radius = int((pXf - Xc) * 0.45)
        dTheta = float((Two_Pi / 360.0) * 3.0)
        Starting_Angle = 0
        Total_Grams = pC + pF + pP
        if(Total_Grams > 0):
            Percent_Carbs   = float(pC / Total_Grams)
            Percent_Fats    = float(pF / Total_Grams)
            Percent_Protein = float(pP / Total_Grams)
            Angle_Carbs   = float(Percent_Carbs * Two_Pi)
            Angle_Fats    = float(Percent_Fats * Two_Pi)
            Angle_Protein = float(Percent_Protein * Two_Pi)
        else:
            return
        #############################################
        #
        # Carbohydrates - medium dark blue
        #
        tmpAngle       = Starting_Angle
        Starting_Angle = tmpAngle + dTheta
        tmpAngle      += Angle_Carbs
        Final_Angle    = tmpAngle - dTheta
        #########################################
        ### Pull Piece out from center a little
        Half_Angle = Final_Angle - Starting_Angle
        Half_Angle = Starting_Angle + (Half_Angle * 0.5)
        xo = Xc + ((Radius * 0.12) * math.cos(Half_Angle))
        yo = Yc + ((Radius * 0.12) * math.sin(Half_Angle))
        #########################################
        ### Draw First Edge of Pie Slice
        x2 = xo + (Radius * math.cos(Starting_Angle))
        y2 = yo + (Radius * math.sin(Starting_Angle))
        self.Draw_Line(pScreen, xo, yo, x2, y2, 0.12, 0.47, 0.71, 2)
        #########################################
        x1 = x2
        y1 = y2
        tmp = (360 / Two_Pi) * Starting_Angle
        tmp = round(tmp, 0)
        sA  = int(tmp)
        tmp = (360 / Two_Pi) * Final_Angle
        tmp = round(tmp, 0)
        fA  = int(tmp)
        for xA in range(sA, fA, 12):
            #####################################
            ### Draw the Out Arc Circle
            tmp = float((Two_Pi / 360) * xA)
            x2 = int(xo + (Radius * math.cos(tmp)))
            y2 = int(yo + (Radius * math.sin(tmp)))
            self.Draw_Line(pScreen, x1, y1, x2, y2, 0.12, 0.47, 0.71, 2)
            x1 = x2
            y1 = y2
        #########################################
        ### Draw Final Edge of Pie Slice
        x2 = xo + (Radius * math.cos(Final_Angle))
        y2 = yo + (Radius * math.sin(Final_Angle))
        self.Draw_Line(pScreen, x1, y1, x2, y2, 0.12, 0.47, 0.71, 2)
        self.Draw_Line(pScreen, xo, yo, x2, y2, 0.12, 0.47, 0.71, 2)
        #############################################
        #
        # Fats - Mustard
        #
        Starting_Angle = tmpAngle + dTheta
        tmpAngle      += Angle_Fats
        Final_Angle    = tmpAngle - dTheta
        #########################################
        ### Pull Piece out from center a little
        Half_Angle = Final_Angle - Starting_Angle
        Half_Angle = Starting_Angle + (Half_Angle * 0.5)
        xo = Xc + ((Radius * 0.12) * math.cos(Half_Angle))
        yo = Yc + ((Radius * 0.12) * math.sin(Half_Angle))
        #########################################
        ### Draw First Edge of Pie Slice
        x2 = xo + (Radius * math.cos(Starting_Angle))
        y2 = yo + (Radius * math.sin(Starting_Angle))
        self.Draw_Line(pScreen, xo, yo, x2, y2, 1, 0.5, 0.05, 2)
        #########################################
        x1 = x2
        y1 = y2
        tmp = (360 / Two_Pi) * Starting_Angle
        tmp = round(tmp, 0)
        sA  = int(tmp)
        tmp = (360 / Two_Pi) * Final_Angle
        tmp = round(tmp, 0)
        fA  = int(tmp)
        for xA in range(sA, fA, 12):
            #####################################
            ### Draw the Out Arc Circle
            tmp = float((Two_Pi / 360) * xA)
            x2 = int(xo + (Radius * math.cos(tmp)))
            y2 = int(yo + (Radius * math.sin(tmp)))
            self.Draw_Line(pScreen, x1, y1, x2, y2, 1, 0.5, 0.05, 2)
            x1 = x2
            y1 = y2
        #########################################
        ### Draw Final Edge of Pie Slice
        x2 = xo + (Radius * math.cos(Final_Angle))
        y2 = yo + (Radius * math.sin(Final_Angle))
        self.Draw_Line(pScreen, x1, y1, x2, y2, 1, 0.5, 0.05, 2)
        self.Draw_Line(pScreen, xo, yo, x2, y2, 1, 0.5, 0.05, 2)
        #############################################
        #
        # Proteins - Leaf Green
        #
        Starting_Angle = tmpAngle + dTheta
        tmpAngle      += Angle_Protein
        Final_Angle    = tmpAngle - dTheta
        #########################################
        ### Pull Piece out from center a little
        Half_Angle = Final_Angle - Starting_Angle
        Half_Angle = Starting_Angle + (Half_Angle * 0.5)
        xo = Xc + ((Radius * 0.12) * math.cos(Half_Angle))
        yo = Yc + ((Radius * 0.12) * math.sin(Half_Angle))
        #########################################
        ### Draw First Edge of Pie Slice
        x2 = xo + (Radius * math.cos(Starting_Angle))
        y2 = yo + (Radius * math.sin(Starting_Angle))
        self.Draw_Line(pScreen, xo, yo, x2, y2, 0.17, 0.63, 0.17, 2)
        #########################################
        x1 = x2
        y1 = y2
        tmp = (360 / Two_Pi) * Starting_Angle
        tmp = round(tmp, 0)
        sA  = int(tmp)
        tmp = (360 / Two_Pi) * Final_Angle
        tmp = round(tmp, 0)
        fA  = int(tmp)
        for xA in range(sA, fA, 12):
            #####################################
            ### Draw the Out Arc Circle
            tmp = float((Two_Pi / 360) * xA)
            x2 = int(xo + (Radius * math.cos(tmp)))
            y2 = int(yo + (Radius * math.sin(tmp)))
            self.Draw_Line(pScreen, x1, y1, x2, y2, 0.17, 0.63, 0.17, 2)
            x1 = x2
            y1 = y2
        #########################################
        ### Draw Final Edge of Pie Slice
        x2 = xo + (Radius * math.cos(Final_Angle))
        y2 = yo + (Radius * math.sin(Final_Angle))
        self.Draw_Line(pScreen, x1, y1, x2, y2, 0.17, 0.63, 0.17, 2)
        self.Draw_Line(pScreen, xo, yo, x2, y2, 0.17, 0.63, 0.17, 2)
        return

    #################################################
    def Draw_Calorie_Bar(self, pScreen=None, pXo=0, pXf=100, pYo=0, pYf=100, pCal=0, pBMR=0):
        Xc = pXo + int((pXf - pXo) * 0.5)
        Yc = pYo + int((pYf - pYo) * 0.5)
        return
    
    #################################################
    def Draw_Rectangles(self, pScreen=None, pXo=0, pXf=100, pYo=0, pYf=100, pR=1, pG=1, pB=0, pOffset=0):
        for x in range(pXo, pXf, 6):
            x3 = x + pOffset
            self.Draw_Line(pScreen, x3, pYo, x3, pYf, pR, pG, pB, 2)
        return

##############################################################
##############################################################


