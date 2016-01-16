import Trip
import datetime
import currency
import time
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config

class CurrencyApp(App):
    def __init__(self):
        super().__init__()
        self.current_date = datetime.date.today().strftime("%Y/%m/%d")
        self.data = Trip.Details()

    def clear(self):
        self.root.ids.status_app.text = ""

    def today_date(self):
        self.root.ids.current_date.text = "Today is:\n{}".format(self.current_date)

    def home_country(self):
        with open("config.txt", "r", encoding= "utf8") as user_file:
            for line in user_file:
                if "," not in line:
                    self.root.ids.home_country.text = line.strip()

    def current_trip_country(self):
        with open("config.txt", "r", encoding= "utf8") as user_file:
            for line in user_file:
                if "," in line:
                    self.data.add(*line.strip("\n").split(","))
        current_country = self.data.current_country(datetime.date.today().strftime("%Y/%m/%d"))
        if current_country == None:
            self.root.ids.trip_location.text = "Current trip location:\n{}".format(self.root.ids.home_country.text)
        else:
            self.root.ids.trip_location.text = "Current trip location:\n{}".format(self.data.current_country(datetime.date.today().strftime("%Y/%m/%d")))

    def get_all_details(self):
        dict = {}
        with open("currency_details.txt", "r", encoding= "utf8") as text_file:
            for line in text_file:
                dict[line.split(",")[0]] = tuple(line.strip().split(","))
        self.root.ids.choose_currency.values = sorted(dict)
        return dict

    def update(self):
        self.root.ids.status_app.text = "Updated at {}".format(time.strftime("%H:%M:%S"))

    def check_valid_home(self):
        try:
            float(self.root.ids.first_input.text)
        except:
            self.root.ids.first_input.text = self.root.ids.first_input.text[:-1]

    def check_valid_location(self):
        try:
            float(self.root.ids.second_input.text)
        except:
            self.root.ids.second_input.text = self.root.ids.second_input.text[:-1]

    def converter(self):
        result = currency.convert(self.root.ids.first_input.text,self.dict[self.root.ids.choose_currency.text][1],self.dict[self.root.ids.home_country.text][1])
        self.root.ids.second_input.text = str(result)
        self.root.ids.status_app.text = "{}({}) to {}({})".format(self.dict[self.root.ids.choose_currency.text][1],self.dict[self.root.ids.choose_currency.text][2],self.dict[self.root.ids.home_country.text][1],self.dict[self.root.ids.home_country.text][2])

    def converter_back(self):
        result = currency.convert(self.root.ids.second_input.text,self.dict[self.root.ids.home_country.text][1],self.dict[self.root.ids.choose_currency.text][1])
        self.root.ids.first_input.text = str(result)
        self.root.ids.status_app.text = "{}({}) to {}({})".format(self.dict[self.root.ids.home_country.text][1],self.dict[self.root.ids.home_country.text][2],self.dict[self.root.ids.choose_currency.text][1],self.dict[self.root.ids.choose_currency.text][2])

    def build(self):
        self.title = "Foreign Exchange Calculator"
        self.root = Builder.load_file("gui.kv")
        self.dict = self.get_all_details()
        self.home_country()
        self.current_trip_country()
        self.today_date()
        return self.root

Config.set('graphics', 'width', 350)
Config.set('graphics', 'height', 700)
Config.set('graphics', 'resizable', False)
CurrencyApp().run()

