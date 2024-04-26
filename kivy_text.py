from kivy.app import App
from kivy.uix.label import Label

class MinhaApp(App):
    def build(self): 
        return Label(
            text='Olá, SENAI!',
            halign='left', # Alinha o texto à esquerdad
            valign='top' # Alinta o texto no topo
            )
    

if __name__ == "__main__":
    MinhaApp().run()