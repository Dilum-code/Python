from tkinter import Label
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class RegistrationApp(App):
    def build(self):
        self.title = "Registration Form"
        layout = BoxLayout(orientation='vertical',padding=30,spacing=10)
        head_label = Label(text="Python User Registration App",font_size=26,bold=True,height=40)
        head_label1 = Label(text="Python User Registration App",font_size=26,bold=True,height=40)

        head_label2 = Label(text="Python User Registration App",font_size=26,bold=True,height=40)

        head_label3 = Label(text="Python User Registration App",font_size=26,bold=True,height=40)

        head_label4 = Label(text="Python User Registration App",font_size=26,bold=True,height=40)

        return layout