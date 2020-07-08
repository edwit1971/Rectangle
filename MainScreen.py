#############################################################
# File Name : MainScreen.py
#
#   Class_Screen1 
#   Displays a Rectangle centered in the screen and when you
#   hit the Rectangles Button a bunch of lines is drawn on
#   the screen and a STOP Button appears and you hit it
#   immediately and you will see how long it took.
#
# Created :   July 2020 
#
#############################################################

import time

from DrawStuff import Draw_Stuff

from kivy.core.window import Window

from kivymd.uix.spinner     import MDSpinner
from kivymd.uix.button      import MDFillRoundFlatButton
from kivymd.uix.textfield   import MDTextField
from kivymd.uix.floatlayout import MDFloatLayout


##############################################################
##############################################################

class Class_Screen1(MDFloatLayout):
    
    #################################################
    def __init__(self, **kwargs):
        super(Class_Screen1, self).__init__(**kwargs)
        ###
        self.Screen_Draw = []
        self.Drawing = Draw_Stuff()
        ###
        self.BRectangle = MDFillRoundFlatButton()
        self.BClear1    = MDFillRoundFlatButton()
        self.BClear2    = MDFillRoundFlatButton()
        self.BStop      = MDFillRoundFlatButton()
        self.TFDisplay  = MDTextField()
        self.Spinner    = MDSpinner(active = False)
        ###
        self.LH = 0
        self.LW = 0
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
        self.LW = self.width
        self.LH = self.height
        if(self.LW >= self.LH):
            min = self.LH
        else:
            min = self.LW
        self.LW = int(min * 0.75)
        self.LH = int(min * 0.75)
        ##############################
        self.Xc = int(self.width  * 0.5)
        self.Yc = int(self.height * 0.5)
        self.Xo = self.Xc - int(self.LW * 0.5)
        self.Xf = self.Xo + self.LW
        self.Yo = self.Yc - int(self.LH * 0.5)
        self.Yf = self.Yo + self.LH
        ##############################
        LHeight = self.Yf - self.Yo
        LHeight = int(LHeight / 3)
        ##############################
        self.Create_ScreenDraw_Widget()
        self.Drawing.Draw_Frame(pScreen = self.Screen_Draw[0], pXo=self.Xo, pXf=self.Xf, pYo=self.Yo, pYf=self.Yf)
        #############################################
        self.Spinner.size_hint = (None, None)
        self.Spinner.width     = int(self.LW * 0.1)
        self.Spinner.height    = self.Spinner.width
        self.Spinner.x         = self.Xc - int(self.Spinner.width * 0.5)
        self.Spinner.y         = self.Yc - int(self.Spinner.height * 0.5)
        if(self.Spinner.parent == None):
            self.add_widget(self.Spinner)
        #############################################
        self.BRectangle.size_hint_y  = None
        self.BRectangle.text   = 'Many Lines'
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
        if(self.BStop.parent == None):
            self.add_widget(self.BStop)
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
        self.TFDisplay.text   = self.StrTime
        self.TFDisplay.multiline = True
        self.TFDisplay.readonly  = True
        self.TFDisplay.hint_text = 'Time (sec)'
        self.TFDisplay.line_color_normal = (0, 0, 0, 1)
        self.TFDisplay.current_hint_text_color = (0, 0, 0, 1)
        if(self.TFDisplay.parent == None):
            self.add_widget(self.TFDisplay)
        ##############################
        self.BRectangle.bind(on_release = self.Press_ManyLines_Button)
        self.BClear1.bind(on_release    = self.Press_Clear1_Button)
        self.BClear2.bind(on_release    = self.Press_Clear2_Button)
        self.BStop.bind(on_release      = self.Press_STOP_Button)
        ##############################
        return
    
    #################################################
    def Create_ScreenDraw_Widget(self):
        max = len(self.Screen_Draw)
        if(max < 1):
            self.Screen_Draw.append(MDFloatLayout(width=self.LW, height=self.LH, x=self.Xc, y=5))
            if(self.Screen_Draw[0].parent == None):
                self.add_widget(self.Screen_Draw[0])
        return
    
    #################################################
    def Delete_ScreenDraw_Widget(self):
        max = len(self.Screen_Draw)
        if(max > 0):
            self.Screen_Draw.pop(0)
        return

    #################################################
    def Press_ManyLines_Button(self, instance):
        self.To = time.time()
        self.Create_ScreenDraw_Widget()
        self.Drawing.Draw_ManyLines(pScreen = self.Screen_Draw[0], \
                                    pXo = self.Xo, \
                                    pXf = self.Xf, \
                                    pYo = self.Yo, \
                                    pYf = self.Yf, \
                                    pR  = 1, \
                                    pG  = 1, \
                                    pB  = 0, \
                                    pOffset = 0)
        self.Drawing.Draw_ManyLines(pScreen = self.Screen_Draw[0], \
                                    pXo = self.Xo, \
                                    pXf = self.Xf, \
                                    pYo = self.Yo, \
                                    pYf = self.Yf, \
                                    pR  = 1, \
                                    pG  = 0, \
                                    pB  = 0, \
                                    pOffset = 1)
        self.Drawing.Draw_ManyLines(pScreen = self.Screen_Draw[0], \
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
        self.Create_ScreenDraw_Widget()
        self.Drawing.Draw_Frame(pScreen = self.Screen_Draw[0], pXo=self.Xo, pXf=self.Xf, pYo=self.Yo, pYf=self.Yf)
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
    def Unbind_All(self):
        self.BRectangle.unbind(on_release = self.Press_ManyLines_Button)
        self.BClear1.unbind(on_release    = self.Press_Clear1_Button)
        self.BClear2.unbind(on_release    = self.Press_Clear2_Button)
        self.BStop.unbind(on_release      = self.Press_STOP_Button)
        return

    #################################################
    def Clear_Drawing_Window(self):
        self.Drawing.Clear_Frame()
        self.Drawing.Clear_Lines()
        self.Delete_ScreenDraw_Widget()
        if(self.Spinner.active):
            self.Spinner.active = False
        else:
            self.Spinner.active = True
        return

    #################################################
    def Clear_Screen(self):
        self.Unbind_All()
        self.Clear_Drawing_Window()
        self.clear_widgets()
        self.canvas.clear()
        if(self.Spinner.active):
            self.Spinner.active = False
        else:
            self.Spinner.active = True
        return

##############################################################
##############################################################

