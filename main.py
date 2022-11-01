from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.properties import ObjectProperty

from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
#from kivymd.theming import ThemableBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.uix.scrollview import ScrollView


class CalcScreen(MDBoxLayout):
    kdo_input = ObjectProperty()
    kso_input = ObjectProperty()
    mmjl_input = ObjectProperty()
    def say_hello(self):
        self.output_label.text = self.calc(self.kdo_input.text, self.kso_input.text, self.mmjl_input.text)
    pass

    def calc(self, kdo, kso, mmlj):
        try:
            kdo_num = float(kdo)
            kso_num = float(kso)
            mmlj_num = float(mmlj)
        except ValueError:
            return "Некорректное значение"
        if (kdo_num * kso_num * mmlj_num == 0):
            return "Параметры должны быть > 0"
        if (kdo_num > 500 or kso_num > 500):
            return "Параметры вне допустимого диапазона (КДО и КСО должны быть < 500 мл.)"

        try:
            return "{0:.0%}".format((kdo_num - kso_num) / (kdo_num * 0.5 + kso_num * 0.5 + mmlj_num/1.05))
        except ValueError as e:
            print(e)

class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(KV)




kv = "main.kv"
class MyMainApp(MDApp):
    def build(self):
        self.root_widget = Builder.load_file(kv)
        return self.root_widget




if __name__ == "__main__":
    MyMainApp().run()
