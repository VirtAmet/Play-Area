import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class CalcGridLayout(GridLayout):
    pass

class CalculatorApp(App):
    
    def build(self):
        return CalcGridLayout()

calcApp=CalculatorApp()
calcApp.run()


    


