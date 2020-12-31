import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
Builder.load_string(
    '''
<MyGrid>:
    fuer:fuer
    masa:masa
    a:a
    GridLayout:
        cols:1
        size:root.width,root.height
        GridLayout:
            cols:2
            Label:
                text:"Introduce la masa"
            TextInput:
                id:masa
                multiline:False
            Label:
                text:"Introduce la acelaracion"
            TextInput:
                id:a
                multiline:False
            Label:
                id:fuer
                text:""
        Button:
            text:"Calcular fuerza"
            on_press:root.fuerza()''')
class MyGrid(Widget):
    masa=ObjectProperty(None)
    a=ObjectProperty(None)
    def fuerza(self):
        masa=float(self.masa.text)
        a=float(self.a.text)
        fuer=masa*a
        self.fuer.text=("La fuerza es {0} N".format(fuer))
class MyApp(App):
    def build(self):
        return MyGrid()
if __name__=="__main__":
    MyApp().run()