#############################################################
# File Name : main.py
#
# Drawing App to help me DEBUG the Kivy Canvas Bug where
# repetitive calls slow down the CPU and Memory builds up
#
# Created :   July 2020 
#############################################################


from kivymd.app import MDApp
from MainScreen import Main_Screen

##############################################################
##############################################################
class LayoutsApp(MDApp):

    def __init__(self, **kwargs):
        super(LayoutsApp, self).__init__(**kwargs)
        self.AppStart = Main_Screen()
        return

    def build(self):
        LayoutsApp.title = 'Drawing App'
        self.AppStart.Initialize()
        return self.AppStart

##############################################################
##############################################################
    
if __name__ == "__main__":
    LayoutsApp().run()

