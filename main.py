import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from get import SimpleSnmp 
#A snmptool é responsável por criar a interface receber os parâmetros e imprimir o resultado
class SnmpToolApp(App):
    h = '::. Get .::'
    #textinput_resultado = ObjectProperty(None)

    def build(self):
        Window.size = (500, 250)
        self.load_kv('main.kv')

    def set_result_form(self, resultado):
        #self.ids["textinput_resultado"].text = resultado
        print (resultado)

#No get values instanciamos um objeto da classe simplegetsnmp (get.py)

    def get_values_form(self, ip, community):
        a= SimpleSnmp(ip,community)
        result = a.GetSNMP()
       #result = result + ' para o IP ' + ip
        #result = result + ' e Community ' + community
        self.set_result_form(result)

if __name__ == "__main__":
    SnmpToolApp().run()
