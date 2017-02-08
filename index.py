import get
import kivy
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.9.0')

__version__ = "0.1.1"

class snmpGetLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(snmpGetLayout, self).__init__(**kwargs)
        self.desloquePilha = 1
        recebe_IP = (None)
        recebe_COMU = (None)


if __name__ == '__main__':
    index().run()
