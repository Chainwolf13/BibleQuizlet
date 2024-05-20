from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.config import Config

Config.set('graphics', 'Resizeable', '0');  # 0 means not resizeable
Config.set('graphics', 'width', '412');  # Makes dimensions for mobile
Config.set('graphics', 'height', '732');


# class SayHello(App):
#     def build(self):
#         self.window = GridLayout()
#         self.window.cols = 1
#         self.window.size_hint = (0.6, 0.7)
#         self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
#         # add widgets to window
#
#         # image widget
#         self.window.add_widget((Image(source="Honeywell.jpg")))
#
#         # label widget
#         self.greeting = Label(text="What is your name?",
#                               font_size=18,
#                               color='#00FFCE'
#                               )
#         self.window.add_widget(self.greeting)
#
#         # text input widget
#         self.user = TextInput(multiline=False,
#                               padding_y=(20, 20),  # defines padding space
#                               size_hint=(1, 0.5),  # width =100% , height is halfed
#                               )
#         self.window.add_widget(self.user)
#
#         # button widget (Creates greet button and activates callback function)
#         self.button = Button(text="Greet",
#                              size_hint=(1, 0),  # button size
#                              bold=True,
#                              background_color='#00FFCE'
#                              )
#         self.button.bind(on_press=self.callback)
#         self.window.add_widget(self.button)
#
#         return self.window
#
#     # Call back function
#     def callback(self, instance):
#         self.greeting.text = "Hello " + self.user.text + "!"


class HomePage(Screen):
    pass


class Q1(Screen):
    pass


class Q2(Screen):
    pass


class Q3(Screen):
    pass


class FinalPage(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


file = Builder.load_file("kivy.kv");


class QuizApp(App):
    def build(self):
        return file

QuizApp().run()

# if __name__ == "__main__":
#     SayHello().run()
