#'If' there's opengl problem, issue the commands 
#pip install kivy.deps.angle
#set KIVY_GL_BACKEND=angle_sdl2 and try running again

#To make it compartible with different python vertion
from __future__ import division, absolute_import
from __future__ import print_function, unicode_literals


from kivy.config import Config 
Config.set('graphics', 'borderless', 'True')
from kivy.core.window import Window

import webbrowser
import random

#calling appropriate module for some functions to work
from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.app import App 
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.textinput import TextInput
from kivy.uix.actionbar import ActionItem
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager,Screen, WipeTransition
from kivy.utils import get_color_from_hex

#For the calculator game
from arithmetic import Arithmetic
from json_settings import json_settings


sm = ScreenManager()

#Calling the other graphics files apart from textilemanager.kv
Window.clearcolor = get_color_from_hex("#16203B")
Builder.load_file("kv/middle.kv")
Builder.load_file("kv/clothes.kv")
Builder.load_file("kv/screens.kv")
Builder.load_file("kv/play.kv")
Builder.load_file("kv/news.kv")

#Main classes in the project
class MiddleScreen(Screen):
    pass

class RecordsScreen(Screen):
    pass

class Records(Screen):
    pass

class NewsScreen(Screen):
    pass

class News(Screen):
    pass
################################################################################################
class OthersScreen(Screen):
    pass

class PlayScreen(Screen):
	pass


class AboutScreen(Screen):
	pass

class MathScreen(Screen, Arithmetic):
	pass


########################################################################################################

class GTPScreen(Screen):
    pass


class WoodinScreen(Screen):
    pass


class HollandScreen(Screen):
    pass

class GTPLine(Screen):
	pass

class WoodinLine(Screen):
	pass

class HollandLine(Screen):
	pass

class LineRectangle(Widget):
    pass

##################################################################################################
class SearchBar(TextInput, ActionItem):
    def __init__(self, *args, **kwargs):
        super(SearchBar, self).__init__(*args, **kwargs)
        self.hint_text='Enter Product'
        self.id='inputText'
    def search(self):
        request = self.text
        return str(request)
#####################################################################################################

#Main textile manager class
class TextileManager(ScreenManager):
    sales_screen = ObjectProperty(None)
    records_screen = ObjectProperty(None)
    news_screen = ObjectProperty(None)
    others_screen = ObjectProperty(None)
    gtp_screen = ObjectProperty(None)
    woodin_screen = ObjectProperty(None)
    holland_screen = ObjectProperty(None)
    about_screen = ObjectProperty()
    kivy_screen_manager = ObjectProperty()



    def __init__(self, **kwargs):
    	super(TextileManager, self).__init__(**kwargs)

    
 ################################################################################################3   

#An app class returning main textile manager class
class TextileManagerApp(App):
	#---------------------------------------------------------------------------
    def build(self):
        m = TextileManager(transition=WipeTransition())
        root = GridLayout(cols=2, padding=50, spacing=50)
        root.add_widget(LineRectangle())
        return TextileManager()

    #----------------------------------------------------------------------------
    def __init__(self, **kwargs):
    	super(TextileManagerApp, self).__init__(**kwargs)


    #----------------------------------------------------------------------------
    def getInputboxText():
        print(instance.text)

    #----------------------------------------------------------------------------

    def changeScreen(self, next_screen):
        #self.root.ids['kivy_screen_manager'].current = 'about_screen'
        self.root.current = 'about_screen'
    #----------------------------------------------------------------------------

    def getText(self):
    	return ("Hey There!\nThis App was built using"
                "[b][ref=kivy] kivy[/ref][/b]\n"
                "Feel free to look at the source code "
                "[b][ref=source]here[/ref][/b].\n"
                "This app is under the [b][ref=Afyacy] Afyacy License[/ref][/b]")

    #------------------------------------------------------------------------------
    def toGtpWeb(self):
        return(webbrowser.open('http://gtpfashion.com/news/'))
    #------------------------------------------------------------------------------
    def toWoodinWeb(self):
        return(webbrowser.open('http://www.woodinfashion.com/'))
    #------------------------------------------------------------------------------
    def toHollandWeb(self):
        return(webbrowser.open('https://www.hollandandholland.com/clothing-collection/'))
    #------------------------------------------------------------------------------
    def toFghWeb(self):
        return(webbrowser.open('https://www.fashionghana.com/#'))
   
    #----------------------------------------------------------------------------

    def on_ref_press(self, instance, ref):
    	_dict = {
            "source": "https://github.com/afyacy/Kivy-App",
            "website": "http://www.afyacy.com",
            "kivy": "http://kivy.org/#home",
            "ttt": "https://github.com/afyacy/Kivy/blob/master/LICENSE"
        }
        #webbrowser.open(_dict[ref])
	

if __name__ == '__main__':
    TextileManagerApp().run()