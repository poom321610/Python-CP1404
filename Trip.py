
class Error(Exception):
    def __init__(self,error_msg):
        self.error_msg = error_msg

class Country:
    def __init__(self,name = "",currency_code = "",currency_symbol = ""):
        self.name = name
        self.currency_code = currency_code
        self.currency_symbol = currency_symbol

    def add_currency(self,amount):
        print(self.currency_symbol + str(amount))

    def __str__(self):
        return '{0} {1} {2}'.format(str(self.name),str(self.currency_code),str(self.currency_symbol))

class Details:
    def __init__(self):
        self.locations = []

    def add(self, country_name, start_date, end_date):
        from _datetime import datetime
        datetime.strptime(start_date,"%Y/%m/%d")
        datetime.strptime(end_date,"%Y/%m/%d")
        try:
            try:
                if start_date > end_date:
                    raise Error("Date is invalid")
            except Error as error_date:
                print(error_date)
                return False

            try:
                for date in self.locations:
                    if start_date in date:
                        raise Error("Date was used")
            except Error as error_date:
                print(error_date)
                False
        except :
            if False:
                self.locations.append(None)
        else:
            self.locations.append((country_name,start_date,end_date))

    def current_country(self,date_string):#check your location
        from _datetime import datetime
        datetime.strptime(date_string,"%Y/%m/%d")
        try:
            for i in self.locations:
                if i[1] <= date_string <= i[2]:
                    return i[0]
                elif self.locations.index(i)+1 == len(self.locations):
                    raise Error("There is no location in that date.")
        except Error as error_location:
            print(error_location)



    def is_empty(self):
        if self.locations:
            return self.locations

if __name__ == "__main__":
    #country test
    country1 = Country("Japan","JPY","¥")
    country1.add_currency(1000)
    print(country1)
    #detail test
    location1 = Details()
    location1.add("Thailand","2015/12/19","2015/12/23")
    location1.add("Thailand","2015/12/20","2015/12/19")
    location1.add("Japan","2015/12/24","2015/12/28")
    location1.add("Thailand","2015/12/20","2015/12/24")
    print(location1.locations[0][1])
    print(location1.locations[0])
    print(location1.locations[0][2])
    print(location1.locations)
    print(location1.current_country("2015/12/24"))
    print(location1.current_country("2016/12/24"))
    print(location1.is_empty())
