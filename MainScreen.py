#############################################################
# File Name : MainScreen.py
#
#             Screen_Intro Class
#             this is the Introduction Screen
#
# Created :   July 2020 
#
#############################################################

import time

from DrawStuff import Draw_Stuff

from kivy.core.window import Window

from kivymd.uix.button      import MDFillRoundFlatButton
from kivymd.uix.textfield   import MDTextField
from kivymd.uix.floatlayout import MDFloatLayout


##############################################################
##############################################################
class Main_Screen(MDFloatLayout):
    
    #################################################
    def __init__(self, **kwargs):
        super(Main_Screen, self).__init__(**kwargs)
        ###
        self.Drawing = Draw_Stuff()
        ###
        self.BRectangle = MDFillRoundFlatButton()
        self.BClear1    = MDFillRoundFlatButton()
        self.BClear2    = MDFillRoundFlatButton()
        self.BStop      = MDFillRoundFlatButton()
        self.TFDisplay  = MDTextField()
        ###
        self.Xo = 0
        self.Xf = 0
        self.Xc = 0
        self.Yo = 0
        self.Yf = 0
        self.Yc = 0
        self.StrTime = ''
        self.To = time.time()
        self.Tf = time.time()
        ###
        return
    
    #################################################
    def Initialize(self):
        ##############################
        # Universal Screen Dimensions
        self.size = Window.size
        LW = self.width
        LH = self.height
        if(LW >= LH):
            min = LH
        else:
            min = LW
        LW = int(min * 0.75)
        LH = int(min * 0.75)
        ##############################
        self.Xc = int(self.width  * 0.5)
        self.Yc = int(self.height * 0.5)
        self.Xo = self.Xc - int(LW * 0.5)
        self.Xf = self.Xo + LW
        self.Yo = self.Yc - int(LH * 0.5)
        self.Yf = self.Yo + LH
        ##############################
        LHeight = self.Yf - self.Yo
        LHeight = int(LHeight / 3)
        ##############################
        self.Draw_Frame()
        ##############################
        self.BRectangle.size_hint_y  = None
        self.BRectangle.text   = 'Rectangles'
        self.BRectangle.height = int(LHeight * 0.3)
        self.BRectangle.x      = 10
        self.BRectangle.y      = self.Yf - int(LHeight * 0.5)
        if(self.BRectangle.parent == None):
            self.add_widget(self.BRectangle)
        ##############################
        self.BStop.size_hint_y  = None
        self.BStop.text   = 'Stop'
        self.BStop.height = self.BRectangle.height
        self.BStop.x      = self.BRectangle.x
        self.BStop.y      = self.BRectangle.y - self.BStop.height - 2
        ##############################
        self.BClear1.size_hint_y  = None
        self.BClear1.text   = 'Clear Drawing'
        self.BClear1.height = self.BRectangle.height
        self.BClear1.x      = self.BRectangle.x
        self.BClear1.y      = self.BRectangle.y - LHeight
        if(self.BClear1.parent == None):
            self.add_widget(self.BClear1)
        ##############################
        self.BClear2.size_hint_y  = None
        self.BClear2.text   = 'Clear Screen'
        self.BClear2.height = self.BRectangle.height
        self.BClear2.x      = self.BRectangle.x
        self.BClear2.y      = self.BClear1.y - LHeight
        if(self.BClear2.parent == None):
            self.add_widget(self.BClear2)
        ##############################
        self.TFDisplay.size_hint = (None, None)
        self.TFDisplay.height = self.Yf - self.Yo
        self.TFDisplay.width  = int((self.width - self.Xf) * 0.9)
        self.TFDisplay.x      = self.Xf + int(self.TFDisplay.width * 0.05)
        self.TFDisplay.y      = self.Yo
        self.TFDisplay.multiline         = True
        self.TFDisplay.readonly          = True
        self.TFDisplay.line_color_normal = (0, 0, 0, 1)
        self.TFDisplay.hint_text         = 'Time (sec)'
        self.TFDisplay.current_hint_text_color = (0, 0, 0, 1)
        if(self.TFDisplay.parent == None):
            self.add_widget(self.TFDisplay)
        self.TFDisplay.text = self.StrTime
        ##############################
        self.BRectangle.bind(on_release = self.Press_Rectangle_Button)
        self.BClear1.bind(on_release    = self.Press_Clear1_Button)
        self.BClear2.bind(on_release    = self.Press_Clear2_Button)
        self.BStop.bind(on_release      = self.Press_STOP_Button)
        ##############################
        return

    #################################################
    def Press_Rectangle_Button(self, instance):
        self.To = time.time()
        self.Clear_Drawing_Window()
        self.Draw_Frame()
        self.Drawing.Draw_Rectangles(pScreen = self, \
                             pXo = self.Xo, \
                             pXf = self.Xf, \
                             pYo = self.Yo, \
                             pYf = self.Yf, \
                             pR  = 1, \
                             pG  = 1, \
                             pB  = 0, \
                             pOffset = 0)
        self.Drawing.Draw_Rectangles(pScreen = self, \
                             pXo = self.Xo, \
                             pXf = self.Xf, \
                             pYo = self.Yo, \
                             pYf = self.Yf, \
                             pR  = 1, \
                             pG  = 0, \
                             pB  = 0, \
                             pOffset = 1)
        self.Drawing.Draw_Rectangles(pScreen = self, \
                             pXo = self.Xo, \
                             pXf = self.Xf, \
                             pYo = self.Yo, \
                             pYf = self.Yf, \
                             pR  = 0, \
                             pG  = 1, \
                             pB  = 1, \
                             pOffset = 2)
        if(self.BStop.parent == None):
            self.add_widget(self.BStop)
        return
    
    #################################################
    def Press_STOP_Button(self, instance):
        self.Tf = time.time()
        Tdiff = self.Tf - self.To
        Ftmp = round(Tdiff, 6)
        self.StrTime += 't = ' + str(Ftmp) + ' (sec)\n'
        self.TFDisplay.text = self.StrTime
        if(self.BStop.parent != None):
            self.remove_widget(self.BStop)
        return

    #################################################
    def Press_Clear1_Button(self, instance):
        self.Clear_Drawing_Window()
        self.Draw_Frame()
        if(self.BStop.parent != None):
            self.remove_widget(self.BStop)
        return

    #################################################
    def Press_Clear2_Button(self, instance):
        self.StrTime = ''
        self.Clear_Screen()
        self.Initialize()
        if(self.BStop.parent != None):
            self.remove_widget(self.BStop)
        return

    #################################################
    def Draw_Frame(self):
        Line_Width = 3
        self.Drawing.Draw_Line(self, self.Xo, self.Yo, self.Xo, self.Yf, 0, 0.39, 0.49, Line_Width)
        self.Drawing.Draw_Line(self, self.Xo, self.Yf, self.Xf, self.Yf, 0, 0.39, 0.49, Line_Width)
        self.Drawing.Draw_Line(self, self.Xf, self.Yo, self.Xf, self.Yf, 0, 0.39, 0.49, Line_Width)
        self.Drawing.Draw_Line(self, self.Xo, self.Yo, self.Xf, self.Yo, 0, 0.39, 0.49, Line_Width)
        return

    #################################################
    def Unbind_All(self):
        self.BRectangle.unbind(on_release = self.Press_Rectangle_Button)
        self.BClear1.unbind(on_release    = self.Press_Clear1_Button)
        self.BClear2.unbind(on_release    = self.Press_Clear2_Button)
        self.BStop.unbind(on_release      = self.Press_STOP_Button)
        return

    #################################################
    def Clear_Drawing_Window(self):
        self.Drawing.Clear_Lines()
        return
    
    #################################################
    def Clear_Screen(self):
        self.Unbind_All()
        self.Drawing.Clear_Lines()
        self.clear_widgets()
        self.canvas.clear()
        return

##############################################################
##############################################################

