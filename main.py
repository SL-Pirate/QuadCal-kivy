#!./.venv/bin/python3

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import quad

class App_Layout(BoxLayout):
    def get_values(self, a1, b1, c1, output_label):
        cal = quad.Cal(a1, b1, c1)
        try:
            rslt = cal.run()
            discriminant_print = rslt['dsc']
            equation = rslt['eqn']
            nature = rslt['nature']
            proceedure = rslt['roots']
            output_label.text = f"{equation} \n{nature} \n{discriminant_print} \n{proceedure}"
        except ValueError:
            output_label.text = "please enter real numbers only. \nUse decimals if needed. \nFill all the three boxes"

class Quadratic_CalculatorApp(App):
#    Window.clearcolor = (191/255, 1, 0, 1)
    pass

if __name__ == "__main__":
    Quadratic_CalculatorApp().run()

'''
__compiling commands__

* build -----> buildozer -v android debug
*deploy -----> buildozer android deploy run logcat

'''