from _datetime import datetime
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config

class Foreign_Exchange_Calculator(App):
    def __init__(self):
        self.trip_location = "LOL"
    #def current_country(self):
    def get_all_details(self):
        dict = {}
        with open("currency_details.txt", "r", encoding= "utf8") as text_file:
            for line in text_file:
                dict[line.split(",")[0]] = tuple(line.strip("\n").split(","))
        self.root.ids.choose_currency.values = sorted(dict)
    def update_press(self):


    def build(self):
        self.root = Builder.load_file("gui.kv")
        return self.root

    def value(self):
        if self.root.ids['result'].text == "hey!":
            self.root.ids['result'].text = "ouch!"
        else:
            self.root.ids['result'].text = "hey!"
Config.set('graphics', 'width', 350)
Config.set('graphics', 'height', 700)
Config.set('graphics', 'resizable', False)
Foreign_Exchange_Calculator().run()
