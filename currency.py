import web_utility

def convert(amount,home_currency_code,location_currency_code):
    if home_currency_code == location_currency_code:
            return -1
    else:
        url_string = "https://www.google.com/finance/converter?a="+ str(amount) + "&from=" + str(home_currency_code) + "&to=" + str(location_currency_code)
        results = web_utility.load_page(url_string)
        result =(results[results.index("result>"):results.index('<input type=submit value="Convert">')-13]).strip("result>" + str(amount) + "*0" + home_currency_code + "= <span class=bld>")
        if "." in result:
            return "{0:,.3f}".format(float(result))
        else:
            return -1


def get_details(currency):
    with open("currency_details.txt", "r", encoding= "utf8") as text_file:
        for line in text_file:
            if currency in line:
                return line.strip("\n")
            elif "\n" not in line:
                return False

def get_all_details():
    dict = {}
    with open("currency_details.txt", "r", encoding= "utf8") as text_file:
        for line in text_file:
            dict[line.split(",")[0]] = tuple(line.strip("\n").split(","))
    return dict

if __name__ == '__main__':

    #testing code
    def check_detail(value,currency):
        if value is False:
            print("{:>15} {:>10} : {:>5}".format("invalid detail",currency,"()"))
        else:
            print("{:>15} {:>10} : {:>5}".format("valid detail",currency,value))

    def check_currency(value,amount,home_currency_code,location_currency_code):
        if value == -1:
            print("{:>24} {:>20} {}->{} {}".format("invalid conversion",float(amount),str(home_currency_code),str(location_currency_code),(value)))
        else:
            print("{:>24} {:>20} {}->{} {}".format("valid conversion",float(amount),str(home_currency_code),str(location_currency_code),(value)))
            print("{:>20} {:>20} {}->{} {}".format("valid conversion reverse",(value),str(location_currency_code),str(home_currency_code),float(amount)))




    check_currency(convert(1,"AUD","AUD"),1,"AUD","AUD")
    check_currency(convert(1,"JPY","ABC"),1,"JPY","ABC")
    check_currency(convert(1,"ABC","USD"),1,"ABC","USD")
    check_currency(convert(10.95,"AUD","JPY"),10.95,"AUD","JPY")
    check_currency(convert(10.95,"AUD","BGN"),10.95,"AUD","BGN")
    check_currency(convert(200.15,"BGN","JPY"),200.15,"BGN","JPY")
    check_currency(convert(100,"JPY","USD"),100,"JPY","USD")
    check_currency(convert(19.99,"USD","BGN"),19.99,"USD","BGN")
    check_currency(convert(19.99,"USD","AUD"),19.99,"USD","AUD")

    check_detail(get_details("Unknown"),"Unknown")
    check_detail(get_details("Japanese"),"Japanese")
    check_detail(get_details("()"),"()")
    check_detail(get_details("Australia"),"Australia")
    check_detail(get_details("Japan"),"Japan")
