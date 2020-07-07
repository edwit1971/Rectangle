#############################################################
# File Name : main.py
#
# Drawing App to help me DEBUG the Kivy Canvas Bug where
# repetitive calls slow down the CPU and Memory builds up
#
# Created :   July 2020 
#############################################################

from kivymd.app import MDApp
from MainScreen import Class_Screen1

##############################################################
##############################################################

class LayoutsApp(MDApp):

    #################################################
    def __init__(self, **kwargs):
        super(LayoutsApp, self).__init__(**kwargs)
        self.cs1 = Class_Screen1()
        return

    def build(self):
        LayoutsApp.title = 'Drawing App'
        self.cs1.Initialize()
        return self.cs1

##############################################################
##############################################################
    
if __name__ == "__main__":
    LayoutsApp().run()

