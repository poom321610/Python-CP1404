from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

class Test(App):

    def build(self):
        self.root = Builder.load_file('try.kv')
        return self.root
    def clear(self):
        if self.root.ids.first_input.text == "" or self.root.ids.second_input == "":
            self.root.ids.status_app.text == ""
Test().run()