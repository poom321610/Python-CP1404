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
        self.current_date = datetime.date.today().strftime("%Y/%m/%d")#today date variable
        self.data = Trip.Details()#Set the data to be Trip.Details object

    def clear(self):#This is for when user type something in the input the message in status app will be clear
        self.root.ids.status_app.text = ""

    def current_trip_country(self):
        self.root.ids.current_date.text = "Today is:\n{}".format(self.current_date)#today date
        with open("config.txt", "r", encoding= "utf8") as user_file:
            for line in user_file:
                if "," not in line:#check for the home country
                    self.root.ids.home_country.text = line.strip()
                elif "," in line:
                    if self.data.add(*line.strip("\n").split(",")):#add other thing except home country
                        self.root.ids.status_app.text = "Invalid detail in file"#wrong data
                    else:
                        self.root.ids.status_app.text = "File is loaded"#correct data
                current_country = self.data.current_country(datetime.date.today().strftime("%Y/%m/%d"))
                if current_country == None:#check user location
                    self.root.ids.trip_location.text = "Current trip location:\n{}".format(self.root.ids.home_country.text)
                else:
                    self.root.ids.trip_location.text = "Current trip location:\n{}".format(current_country)

    def spinner(self):
        dict = {}
        with open("currency_details.txt", "r", encoding= "utf8") as text_file:
            for line in text_file:
                dict[line.split(",")[0]] = tuple(line.strip().split(","))
                self.root.ids.choose_currency.values = sorted(dict)
        return dict

    def update(self):
        self.root.ids.status_app.text = "Updated at {}".format(time.strftime("%H:%M:%S"))
        self.root.ids.first_input.disabled = False
        self.root.ids.second_input.disabled = False
        if self.root.ids.choose_currency.text == "":
            self.root.ids.choose_currency.text = self.root.ids.home_country.text

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
        if result == -1:
            self.root.ids.first_input.disabled = True
            self.root.ids.second_input.disabled = True
        else:
            self.root.ids.second_input.text = str(result)
            self.root.ids.status_app.text = "{}({}) to {}({})".format(self.dict[self.root.ids.choose_currency.text][1],self.dict[self.root.ids.choose_currency.text][2],self.dict[self.root.ids.home_country.text][1],self.dict[self.root.ids.home_country.text][2])

    def converter_back(self):
        result = currency.convert(self.root.ids.second_input.text,self.dict[self.root.ids.home_country.text][1],self.dict[self.root.ids.choose_currency.text][1])
        if result == -1:
            self.root.ids.first_input.disabled = True
            self.root.ids.second_input.disabled = True
        else:
            self.root.ids.first_input.text = str(result)
            self.root.ids.status_app.text = "{}({}) to {}({})".format(self.dict[self.root.ids.home_country.text][1],self.dict[self.root.ids.home_country.text][2],self.dict[self.root.ids.choose_currency.text][1],self.dict[self.root.ids.choose_currency.text][2])

    def build(self):
        self.title = "Foreign Exchange Calculator"
        self.root = Builder.load_file("gui.kv")
        self.dict = self.spinner()
        self.current_trip_country()
        return self.root

Config.set('graphics', 'width', 350)
Config.set('graphics', 'height', 700)
Config.set('graphics', 'resizable', False)
if __name__ == "__main__":
    CurrencyApp().run()

