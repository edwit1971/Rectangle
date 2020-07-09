#############################################################
# File Name : MainScreen.py
#
#   Class_Screen1 
#
#   Start out by hitting the PRESS ME Button when the App
#   starts.  This will clear the Lines Drawn.
#
#   Then a new Button appears that says NOW PRESS ME and
#   when you hit it lines will be drawn on the screen.
#
#   a TIMER Button will appear.  Press it immediatly EVERY
#   time it appears to be consistent.
#
#   You should notice that as you keep pressing
#   PRESS ME and then NOW PRESS ME and then
#   PRESS ME and then NOW PRESS ME repeatedly the
#   time gets bigger and bigger meaning the program is
#   SLOWING DOWN!!!!!
#
#   But the NOW PRESS ME Button clears all the lines from
#   the CANVAS instruction list and clears the canvas. So
#   why is the app getting SLOWER AND SLOWER??????????
#
#
# Created :   July 2020 
#
# Ed Witkowski III
# EdWit1971@gmail.com
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

class Class_Screen1(MDFloatLayout):
    
    #################################################
    def __init__(self, **kwargs):
        super(Class_Screen1, self).__init__(**kwargs)
        ###
        self.Drawing = Draw_Stuff()
        ###
        self.Now_Press_Me_Button = MDFillRoundFlatButton()
        self.Press_Me_Button = MDFillRoundFlatButton()
        self.Clear_Screen_Button = MDFillRoundFlatButton()
        self.BStop      = MDFillRoundFlatButton()
        self.TFDisplay  = MDTextField()
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
        self.LW = int(min * 0.5)
        self.LH = int(min * 0.5)
        ##############################
        self.Xc = int(self.width  * 0.5)
        self.Yc = int(self.height * 0.5)
        self.Xo = self.Xc - int(self.LW * 0.5)
        self.Xf = self.width - 5
        self.Yo = self.Yc - int(self.height * 0.5) + 5
        self.Yf = self.height - 5
        ##############################
        LHeight = self.height
        LHeight = int(LHeight / 16)
        ##############################
        self.Clear_Drawing_Window()
        self.Drawing.Draw_Frame(pScreen = self, pXo=self.Xo, pXf=self.Xf, pYo=self.Yo, pYf=self.Yf)
        self.Drawing.Show_Instructions(pScreen = self)
        ##############################
        self.Now_Press_Me_Button.size_hint_y  = None
        self.Now_Press_Me_Button.text   = 'NOW PRESS ME'
        self.Now_Press_Me_Button.height = LHeight
        self.Now_Press_Me_Button.x      = int(self.Xo * 0.1)
        self.Now_Press_Me_Button.y      = self.height - int(LHeight * 2)
        if(self.Now_Press_Me_Button.parent != None):
            self.remove_widget(self.Now_Press_Me_Button)
        ##############################
        self.BStop.size_hint_y  = None
        self.BStop.text   = 'TIMER'
        self.BStop.height = self.Now_Press_Me_Button.height
        self.BStop.x      = self.Now_Press_Me_Button.x
        self.BStop.y      = self.Now_Press_Me_Button.y - int(LHeight * 2)
        if(self.BStop.parent != None):
            self.remove_widget(self.BStop)
        ##############################
        self.Press_Me_Button.size_hint_y  = None
        self.Press_Me_Button.text   = 'PRESS ME'
        self.Press_Me_Button.height = self.Now_Press_Me_Button.height
        self.Press_Me_Button.x      = self.Now_Press_Me_Button.x
        self.Press_Me_Button.y      = self.BStop.y - int(LHeight * 2)
        if(self.Press_Me_Button.parent == None):
            self.add_widget(self.Press_Me_Button)
        ##############################
        self.Clear_Screen_Button.size_hint_y  = None
        self.Clear_Screen_Button.text   = 'Clear Screen'
        self.Clear_Screen_Button.height = self.Now_Press_Me_Button.height
        self.Clear_Screen_Button.x      = self.Now_Press_Me_Button.x
        self.Clear_Screen_Button.y      = self.Press_Me_Button.y - int(LHeight * 2)
        if(self.Clear_Screen_Button.parent == None):
            self.add_widget(self.Clear_Screen_Button)
        ##############################
        Y1 = self.Clear_Screen_Button.y - LHeight
        self.TFDisplay.size_hint = (None, None)
        self.TFDisplay.height = int(Y1 * 0.9)
        self.TFDisplay.width  = int(self.Xo * 0.8)
        self.TFDisplay.x      = self.Now_Press_Me_Button.x
        self.TFDisplay.y      = self.Clear_Screen_Button.y - int(LHeight * 2) - self.TFDisplay.height
        self.TFDisplay.text   = self.StrTime
        self.TFDisplay.multiline = True
        self.TFDisplay.readonly  = True
        self.TFDisplay.hint_text = 'Time (sec)'
        self.TFDisplay.helper_text = 'Press TIMER when you see it'
        self.TFDisplay.helper_text_mode = 'persistent'
        self.TFDisplay.line_color_normal = (0, 0, 0, 1)
        self.TFDisplay.current_hint_text_color = (0, 0, 0, 1)
        if(self.TFDisplay.parent == None):
            self.add_widget(self.TFDisplay)
        ##############################
        self.Now_Press_Me_Button.bind(on_release = self.Press_Now_Press_Me_Button)
        self.Press_Me_Button.bind(on_release = self.Press_Press_Me_Button)
        self.Clear_Screen_Button.bind(on_release = self.Press_Clear_Screen_Button)
        self.BStop.bind(on_release = self.Press_STOP_Button)
        ##############################
        return

    #################################################
    def Press_Now_Press_Me_Button(self, instance):
        self.To = time.time()
        self.Clear_Drawing_Window()
        self.Drawing.Draw_ManyLines(pScreen = self, \
                                    pXo = self.Xo, \
                                    pXf = self.Xf, \
                                    pYo = self.Yo, \
                                    pYf = self.Yf, \
                                    pR  = 0, \
                                    pG  = 1, \
                                    pB  = 1, \
                                    pOffset = 2)
        self.Drawing.Show_Instructions(pScreen = self)
        #############################################
        if(self.TFDisplay.parent == None):
            self.add_widget(self.TFDisplay)
        if(self.Clear_Screen_Button.parent == None):
            self.add_widget(self.Clear_Screen_Button)
        if(self.BStop.parent == None):
            self.add_widget(self.BStop)
        if(self.Press_Me_Button.parent == None):
            self.add_widget(self.Press_Me_Button)
        #############################################
        if(self.Now_Press_Me_Button.parent != None):
            self.remove_widget(self.Now_Press_Me_Button)
        #############################################
        return

    #################################################
    def Press_STOP_Button(self, instance):
        self.Tf = time.time()
        Tdiff = self.Tf - self.To
        Ftmp = round(Tdiff, 6)
        self.StrTime += 't = ' + str(Ftmp) + ' (sec)\n'
        self.TFDisplay.text = self.StrTime
        #############################################
        if(self.BStop.parent != None):
            self.remove_widget(self.BStop)
        #############################################
        return

    #################################################
    def Press_Press_Me_Button(self, instance):
        self.Clear_Drawing_Window()
        self.Drawing.Draw_Frame(pScreen = self, pXo=self.Xo, pXf=self.Xf, pYo=self.Yo, pYf=self.Yf)
        self.Drawing.Show_Instructions(pScreen = self)
        #############################################
        if(self.Now_Press_Me_Button.parent == None):
            self.add_widget(self.Now_Press_Me_Button)
        if(self.TFDisplay.parent == None):
            self.add_widget(self.TFDisplay)
        if(self.Clear_Screen_Button.parent == None):
            self.add_widget(self.Clear_Screen_Button)
        #############################################
        if(self.BStop.parent != None):
            self.remove_widget(self.BStop)
        if(self.Press_Me_Button.parent != None):
            self.remove_widget(self.Press_Me_Button)
        #############################################
        return

    #################################################
    def Press_Clear_Screen_Button(self, instance):
        self.StrTime = ''
        self.Clear_Screen()
        self.Initialize()
        #############################################
        if(self.Now_Press_Me_Button.parent == None):
            self.add_widget(self.Now_Press_Me_Button)
        if(self.TFDisplay.parent == None):
            self.add_widget(self.TFDisplay)
        if(self.Press_Me_Button.parent == None):
            self.add_widget(self.Press_Me_Button)
        if(self.Clear_Screen_Button.parent == None):
            self.add_widget(self.Clear_Screen_Button)
        #############################################
        if(self.Now_Press_Me_Button.parent != None):
            self.remove_widget(self.Now_Press_Me_Button)
        if(self.BStop.parent != None):
            self.remove_widget(self.BStop)
        #############################################
        return

    #################################################
    def Unbind_All(self):
        self.Now_Press_Me_Button.unbind(on_release = self.Press_Now_Press_Me_Button)
        self.Press_Me_Button.unbind(on_release = self.Press_Press_Me_Button)
        self.Clear_Screen_Button.unbind(on_release = self.Press_Clear_Screen_Button)
        self.BStop.unbind(on_release = self.Press_STOP_Button)
        return

    #################################################
    def Clear_Drawing_Window(self):
        self.Drawing.Clear_IG()
        return

    #################################################
    def Clear_Screen(self):
        self.Unbind_All()
        self.Clear_Drawing_Window()
        self.clear_widgets()
        self.canvas.clear()
        return

##############################################################
##############################################################

